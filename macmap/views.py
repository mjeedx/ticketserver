import sys

from django.http import JsonResponse

from macmap.models import Sw_db, Mac_list
from django.shortcuts import render, render_to_response
from pysnmp.hlapi import nextCmd, SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectIdentity, \
    ObjectType


OID = "1.3.6.1.2.1.17.4.3.1.2"

def int_to_mac(str_mac):
    macs = str_mac.split('.')
    print("This is str_mac", str_mac)
    i = 0
    ma = []
    for x in range(0, 6):
        maca = macs[i]
        print("iter ", x, )
        print(i, " ", ma)
        if len(maca) == 1:
            print("iflen ", x)
            a = hex(int(maca)).replace("x", "")
        else:
            a = hex(int(maca))[2:]
            print("elselen", a)
        if len(a) == 1:
            a = "0" + a
        ma.append(a)
        i = i + 1
    return ma[0] + ":" + ma[1] + ":" + ma[2] + ":" + ma[3] + ":" + ma[4] + ":" + ma[5]


def mac_request(request):
    def walk(host, oid):
        for (errorIndication,
             errorStatus,
             errorIndex,
             varBinds) in nextCmd(SnmpEngine(),
                                  CommunityData('public'),
                                  UdpTransportTarget((host, 161)),
                                  ContextData(),
                                  ObjectType(ObjectIdentity(oid)),
                                  lookupMib=False,
                                  lexicographicMode=False):

            if errorIndication:
                print(errorIndication, file=sys.stderr)
                break

            elif errorStatus:
                print('%s at %s' % (errorStatus.prettyPrint(),
                                    errorIndex and varBinds[int(errorIndex) - 1][0] or '?'), file=sys.stderr)
                break

            else:
                for varBind in varBinds:
                    # print('%s = %s' % varBind)
                    mac = '%s = %s' % varBind
                    mac = mac[23:]
                    mac = mac.split(" = ")
                    mac_list.append(mac)

        return mac_list

    sw_ip = Sw_db.objects.filter(enable=True)

    for sw in sw_ip:
        mac_list = []
        print("swIP= ", sw.ipv4)
        mac_list = walk(sw.ipv4, OID)
        for ii in range(len(mac_list)):
            mac_list[ii][0] = int_to_mac(mac_list[ii][0]).upper()
            print(mac_list[ii])
        list = []
        sw_id = Sw_db.objects.get(ipv4=sw.ipv4)
        for i in mac_list:
            list.append(Mac_list(sw_id=sw_id,
                                 mac=i[0], port=i[1]))
        Mac_list.objects.filter(sw_id=sw_id).delete() #Удаляем старые записи
        Mac_list.objects.bulk_create(list) # Записываем в базу
    return JsonResponse({'status': 'ok'})


def macmap(request): # Показать таблицу адресов
    args = {"mac_list": Mac_list.objects.all(),
            "sw_db": Sw_db.objects.all()}
    return render_to_response('macmap.html', args)
