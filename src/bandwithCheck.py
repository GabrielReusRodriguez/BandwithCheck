#!/bin/env python3

# -*- coding: utf-8 -*-

#Programa para testear el ancho de banda disponible 

# https://ricardogeek.com/monitorear-la-velocidad-del-internet-con-python/

import matplotlib.pyplot as plotter
import matplotlib.ticker as ticker
import speedtest
import datetime

import csv

#Declaracion de constantes
MAX_ITERATIONS = 10

#Variables iniciales
servers = []
times = []
download = []
upload = []
iteration = 0

#Inicio del programa
print("inicio")

#Init de speedtest
tester = speedtest.Speedtest()
tester.get_servers(servers)
tester.get_best_server()

#Init de escribir fichero csv.
#with open('test.csv', mode='w', newline='' ) as speedcsv:
#    
#    csv_writer = csv.DictWriter(speedcsv,
#                                fieldnames=['time', 'downspeed', 'upspeed'])
#    csv_writer.writeheader()
#
#    #Bucle de lógica
#    while iteration < MAX_ITERATIONS:
#
#        time = datetime.datetime.now().strftime("%H:%M:%S")
#        downspeed = round((round(tester.download()) / 1048576), 2)
#        #Utilizamos pre_allocate = False pare evitar errores de memoria.
#        upspeed = round((round(tester.upload( pre_allocate=False )) / 1048576), 2)
#        print(f"iteration: {iteration+1}, time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
#        csv_writer.writerow({
#            'time': time,
#            'downspeed': downspeed,
#            "upspeed": upspeed
#        })
#        speedcsv.flush()
#        iteration = iteration + 1

while iteration < MAX_ITERATIONS:

    time = datetime.datetime.now().strftime("%H:%M:%S")
    downspeed = round((round(tester.download()) / 1048576), 2)
    #Utilizamos pre_allocate = False pare evitar errores de memoria.
    upspeed = round((round(tester.upload( pre_allocate=False )) / 1048576), 2)
    print(f"iteration: {iteration+1}, time: {time}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
    
    times.append(str(time))
    download.append(float(downspeed))
    upload.append(float(upspeed))

    iteration = iteration + 1

avgDownSpeed = 0
avgUpSpeed = 0

#Calculo media down
for down in download:
    avgDownSpeed = avgDownSpeed + down

avgDownSpeed = round(float ( avgDownSpeed / MAX_ITERATIONS),2)

#Calculo media up
for up in upload:
    avgUpSpeed = avgUpSpeed + up

avgUpSpeed = round(float ( avgUpSpeed / MAX_ITERATIONS),2)



print(f"\naverage downspeed: {avgDownSpeed} Mb/s, upspeed: {avgUpSpeed} Mb/s")

#Init del plotter

#Se generan los reportes
#with open('test.csv', 'r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     next(csvfile)
#     for row in plots:
#        times.append(str(row[0]))
#        download.append(float(row[1]))
#        upload.append(float(row[2]))

plotter.figure('speedtest', [30, 30])
plotter.plot(times, download, label='download', color='r')
plotter.plot(times, upload, label='upload', color='b')
plotter.xlabel('time')
plotter.ylabel('speed in Mb/s')
plotter.title("internet speed")
plotter.legend()
plotter.show()
#plotter.savefig('test_graph.jpg', bbox_inches='tight')


#print(times, "\n", download, "\n", upload)


#print(tester.download())
#print(tester.upload())

#tester.results.share()
#print(tester.download(),tester.upload())

print("final")
