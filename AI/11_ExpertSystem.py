def expertsystem():
  print("Welcome to Hospital Expert System how may I be of assistance? ")
  

  while True:
    problem = input("Please enter your issue: ").lower()

    if problem == "exit":
      print("Thank you for using the system Have a good day")
      break

    elif "visiting" and "hours" in problem:
      print("Visiting Hours are evening 17.00 to 20.00")

    elif "appointment" and "book" in problem:
      print("Please visit the front desk besides the entrance for booking an appointment a human representative will be with you shortly")

    elif "appointment" and "cancel" in problem:
      print("Appointment cancelled to reschedule/rebook please visit premises")

    elif "Collect" and "reports" in problem:
      print("Digital reports have been sent to registered mobile id, please collect physical reports from lab")
  
    else:
      print("Unable to resolve please contact tech support or human representative")

expertsystem()