"""5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице."""


import subprocess

ping = [['ping', '-c 4', 'youtube.com'], ['ping', '-c 4', 'yandex.ru']]
for args in ping:

    print(f'{10*"*"} ping веб-ресурса {args[2]} {10*"*"}')
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


"""РЕЗУЛЬТАТ
********** ping веб-ресурса youtube.com **********
PING youtube.com (64.233.164.136): 56 data bytes

64 bytes from 64.233.164.136: icmp_seq=0 ttl=110 time=39.239 ms

64 bytes from 64.233.164.136: icmp_seq=1 ttl=110 time=44.011 ms

64 bytes from 64.233.164.136: icmp_seq=2 ttl=110 time=35.975 ms

64 bytes from 64.233.164.136: icmp_seq=3 ttl=110 time=42.360 ms



--- youtube.com ping statistics ---

4 packets transmitted, 4 packets received, 0.0% packet loss

round-trip min/avg/max/stddev = 35.975/40.396/44.011/3.074 ms

********** ping веб-ресурса yandex.ru **********
PING yandex.ru (5.255.255.77): 56 data bytes

64 bytes from 5.255.255.77: icmp_seq=0 ttl=55 time=16.998 ms

64 bytes from 5.255.255.77: icmp_seq=1 ttl=55 time=27.873 ms

64 bytes from 5.255.255.77: icmp_seq=2 ttl=55 time=30.676 ms

64 bytes from 5.255.255.77: icmp_seq=3 ttl=55 time=17.563 ms



--- yandex.ru ping statistics ---

4 packets transmitted, 4 packets received, 0.0% packet loss

round-trip min/avg/max/stddev = 16.998/23.277/30.676/6.082 ms


"""