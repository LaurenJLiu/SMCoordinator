import csv

fileName = input("Move Number: ") + '.csv'

with open(fileName, 'rt', encoding='CP1252') as csvfile:
    reader = csv.reader(csvfile)
    row = [r for r in reader]

#------------------------------------------

moveNum = row[4][2]
moveDate = row[5][2]
moveTime = row[6][2]
mcName = row[1][2]
mcPhone = row[2][2]
items = row[50][1]

leadMover = row[9]
leadMovers = [[leadMover, 'Lead Mover']]

driver1 = row[12]
driver2 = row[13]
driver3 = row[14]
drivers = [[driver1, 'Driver #1'], [driver2, 'Driver #2'], [driver3, 'Driver #3']]

if driver1[2] == leadMover[2]:
    drivers[0] = [driver1, 'Lead Mover & Driver #1']
    leadMover[2] = ""

mover1 = row[17]
mover2 = row[18]
mover3 = row[19]
mover4 = row[20]
mover5 = row[21]
movers = [[mover1, 'Mover'], [mover2, 'Mover'], [mover3, 'Mover'], [mover4, 'Mover'], [mover5, 'Mover']]

tempTeam = [leadMovers, drivers, movers]
moveTeam = []
for x in tempTeam:
    for y in x:
        moveTeam.append(y)

location1 = row[24]
location2 = row[25]
location3 = row[26]
location4 = row[27]
location5 = row[28]
location6 = row[29]
location7 = row[30]
location8 = row[31]
location9 = row[32]
location10 = row[33]
locations = [location1, location2, location3, location4, location5, location6, location7, location8, location9, location10]

itinerary1 = row[37]
itinerary2 = row[38]
itinerary3 = row[39]
itinerary4 = row[40]
itinerary5 = row[41]
itinerary6 = row[42]
itinerary7 = row[43]
itinerary8 = row[44]
itinerary9 = row[45]
itinerary10 = row[46]
itineraries = [itinerary1, itinerary2, itinerary3, itinerary4, itinerary5, itinerary6, itinerary7, itinerary8, itinerary9, itinerary10]

#------------------------------------------
moveItinerary = 'Itinerary' + moveNum + '.html'

with open(moveItinerary, 'w') as f:
    f.write('<html>\n')
    f.write('<body>\n')

    #--------------------------------------
    f.write('<font size="3" style="color:black">')
    f.write('<p>Hi All,')
    f.write('<p>Thank you for agreeing to take on <b><font size="4">Move #' + moveNum + ' on ' + moveDate + ' @ ' + moveTime + '</font></b>' )
    f.write('<p>Below is essential information about the move, and the presumed itinerary. Please make sure you have this email available on your phone as a reference. I will also be available as a support for you during the time of this move, @ <b><font style="color:blue">' + mcPhone +'</font></b>')
    f.write('<br>I hope you do not mind, I have put your phone numbers below for communication purposes during the move.')
    f.write('<p><p>Let me know if you have any questions or concerns, I am happy to clarify!')

    #--------------------------------------
    f.write('<p><b><u>Move Team:</u></b><p>')

    for person in moveTeam:
        personName = person[0][2]
        personPosition = person[1]
        personPhone = person[0][3]

        if personName != "":
            f.write('<b><font style="color:green">' + personName + '</font></b> (' + personPosition + ') <b>' + personPhone + '</b><br>')

    #--------------------------------------
    f.write('<p><b><u>Vehicle Information:</u></b><p>')

    for driver in drivers:
        driverName = driver[0][2]
        vehicleNumber = driver[0][4]
        reservationTime = driver[0][5] + '-' + driver[0][6]
        vehicleDescription = driver[0][9]
        locationInfo = driver[0][10]
        operatingInfo = driver[0][11]

        if driverName != "":
            f.write('<b><font style="color:green">' + driverName + '</font></b>' + ' #' + vehicleNumber + ' ' + vehicleDescription + '</b>')
            f.write('<br><font size="2"><u><mark>Reserved from: ' + reservationTime + '</mark></u></font>')
            f.write('<br><font style="color:gray">' + locationInfo)
            f.write('<br>' + operatingInfo + '</font><p>')

    f.write('<p><font style="color:red"><u>IMPORTANT NOTES FOR DRIVERS:</u> Please refrain from taking HWY 407 ETR, as it is a toll route and we do not have the funds to pay for the associated fees.')
    f.write('<br>Also, the vehicles must be returned to the location with at least 1/4 tank of gas. If you fill up, GET A RECEIPT so that you can be reimbursed.</font>')

    #--------------------------------------
    f.write('<p><b><u>Locations:</u></b><p>')

    for location in locations:
        if location[3] != "":
            locationType = location[2]
            locationAddress = location[3]
            f.write('<i><font style="color:orange">' + locationType + ':</font></i>       ' + locationAddress + '<br>')

    f.write('<p>')

    for driver in drivers:
        driverName = driver[0][2]
        route = driver[0][8]

        if driverName != "":
            f.write('<b><font style="color:green">' + driverName + '</font></b>     <a href="' + route + '">GMaps Full Route</a><br>')

    #--------------------------------------
    f.write('<p><b><u>Itinerary:</u></b>')

    for driver in drivers:
        driverName = driver[0][2]
        pickupTime = driver[0][7]
        vehicleDescription = driver[0][9]

        if driverName != "":
            f.write('<p><mark><u>' + pickupTime + ':</u></mark>        ')
            f.write('<b><font style="color:green">' + driverName + '</font></b> will pick up <b>' + vehicleDescription + '</b><br>')

            for mover in movers:
                moverName = mover[0][2]
                moversDriver = mover[0][4]

                if driverName == moversDriver:
                    f.write('<br><b><font style="color:green">' + moverName + '</font></b>, if you could meet <b><font style="color:green">' + driverName + ' </font></b>at this Enterprise Vehicle <b>(' + vehicleDescription + ') at ' + pickupTime + '</b>, that would be great! Exact details can be found under "Vehicle Information". If you are unable to get to this location, please "Reply All" to this email so we all know, and we will see if there is another option.')

    for itinerary in itineraries:
        if itinerary[1] != "":
            startTime = itinerary[1]
            endTime = itinerary[2]
            time = startTime + '-' + endTime
            driveTime = itinerary[4]

            f.write('<p><mark><u>' + time + ':</u></mark>        ')
            f.write(itinerary[8] + ' (Approx. ' + driveTime + ' min. drive).')

    f.write('<p><mark><u>' + endTime + ':</u></mark>        ')
    f.write('When complete, ')

    for driver in drivers:
        driverName = driver[0][2]
        vehicleDescription = driver[0][9]

        if driverName != "":
            f.write('<br><b><font style="color:green">' + driverName + '</font></b> will drop off <b>' + vehicleDescription + '</b><br>')

    #--------------------------------------
    f.write('<p><b><u>Notes About This Move:</u></b><ul>')
    f.write('<li><u>Items to be moved:</u> ' + items + '</ul>')

    #--------------------------------------
    f.write('<p><b><u>Security Reminders:</u></b><ul>')
    f.write('<li><b><u>NEW INFORMATION:</u> In recognition of the chronic bed bug problem in Toronto and the risk of exposure to SMT volunteers, please take the following precautions when returning home from a move to prevent the spread of bed bugs: Remove and dry your clothes, place them in a plastic bag and put them in the dryer on high heat immediately upon returning to your home. </b>')
    f.write('For detailed instructions on how to prevent bed bugs please see the Movers Manual <a href="https://docs.google.com/a/sheltermovers.com/document/d/1F04cKdrxSx3WgfAzzKIJmaO0dzbmewzhUe4092I36x0/edit?usp=sharing">here</a>.')
    f.write('<li>Movers will not come in physical contact with clients. A handshake initiated by the client is ok.')
    f.write('<li>Movers are always vigilant for changes to the risk associated with the move and communicate with each other if something doesn\'t feel / seem right.')
    f.write('<li>Movers are careful not to injure themselves or put their colleagues at risk when moving items.')
    f.write('<li>Addresses or location information contained on movers\' phones will be erased immediately following a move.')
    f.write('<li>There will be debriefing and follow-up emails a few days after the move.</ul>')

    #--------------------------------------
    f.write('<p><b><u>Items to Bring:</u></b><ul>')
    f.write('<li>Closed-toe shoes')
    f.write('<li>Cell phone battery charger')
    f.write('<li>Work gloves (as needed)')
    f.write('<li>Any questions or concerns should be directed to <b>' + mcName + ' <font style="color:blue">'+ mcPhone + '</b></font></ul>')

#------------------------------------------
    f.write('</body>\n')
    f.write('</html>\n')
    f.close()
