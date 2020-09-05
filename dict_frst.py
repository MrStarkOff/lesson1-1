grad_temp = {
    "city": "Москва",
    "temp": "20"
}
print(grad_temp["city"])

print(grad_temp)

grad_temp["temp"] = int(grad_temp["temp"]) -5

print(grad_temp)

print(grad_temp.get("counrty", "Россия"))

print(len(grad_temp))
grad_temp["date"] = "27.05.2019"
print(grad_temp)
print(len(grad_temp))

#grad_temp["temp"] = grad_temp["temp"-5]
#print(grad_temp)