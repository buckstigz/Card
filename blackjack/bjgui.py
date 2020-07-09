from guizero import App, PushButton

app = App(title="Welcome to Blackjack", width=500, height=400, layout="grid")
hit = PushButton(app, text="Hit", grid=[1, 3], align="left")
stick = PushButton(app, text="Stick", grid=[2, 3], align="top")
bet = PushButton(app, text="Bet", grid=[3, 3], align="right")

app.display()