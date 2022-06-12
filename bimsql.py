print("\nWELCOME!")
print("\nINSERTION TOOL MYSQL(QUERY GENERATOR)---->BY XERY PROGRAMMER")

airportlist=input("\nEnter the Airport Names Followed by Comma ',': ").split(",")
airportlistlen=len(airportlist)

airportcountry=input("\nEnter the Airport Country Followed by Comma ',': ").split(",")

airportlocation=input("\nEnter the Airport Location Followed by Comma ',': ").split(",")

airportIATA=input("\nEnter the Airport IATA Code Followed by Comma ',': ").split(",")

output=[]
for x in range(airportlistlen):
    a=f"('{airportlist[x]}'.'{airportcountry[x]}'.'{airportlocation[x]}'.'{airportIATA[x]}')"
    output.append(a)
    

print("\n<-----------------------------COPY FROM HERE------------------------------------------>")
print(f"\nINSERT INTO airport (airport_name,airport_country,airport_location,IATA_code) VALUES")

listToStr = ' ,'.join(map(str, output))
listToStr[:-1]
comma_replace=listToStr.replace(",",",\n")
point_replace=comma_replace.replace(".",",")
print(point_replace+";")
    
print("\n<-----------------------------COPY TILL HERE------------------------------------------>")


