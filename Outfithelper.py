#import PIL
#from PIL import Image

print("This is an app to help with clothe recommendations based on the weather.")

rain = int(input("What is the chance of rain in your location today?"))

temperature = int(input("What is the celsius temperature of your location today"))
def recommend_outfit(rain, temperature):
    if rain > 30 and rain < 50:
        print("You should have umbrella handy")
        umbrella = Image.open("Umbrella.jpg")
        umbrella.show()
    elif rain > 50:
        print("Strong chance it rains today, you should definitely keep a raincoat!")
        raincoat =Image.open("Raincoat.jpg")
        raincoat.show()
    elif rain <30:
        print("looks like it will be dry today!")

    if temperature < 14:
        print("You're going to have a cold day aheand, make sure to layer up!")
        coldday = Image.open("Colddays.jpg")
        coldday.show()
    elif temperature > 14 and temperature <19:
        print("It's a cool day today, a cardigan is not a bad idea")
        coolday = Image.open("Early fall.jpg")
        coolday.show()
    else:
        print("You'll have a warm day today. Light, airy clothes are the way to go")
        airy = Image.open("For warmer weather.jpg")
        airy.show()
recommend_outfit(rain, temperature)
    
    
