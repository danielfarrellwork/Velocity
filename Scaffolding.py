'''A file to display and monitor pay rate and effort'''
import pandas as pd
from matplotlib import pyplot as plt
#Import rate history
raw_rates_df = pd.read_excel(r"C:\\Users\\usdf659971\\OneDrive - WSP O365\\Education\\Grad School\\Education.xlsx", sheet_name="Scaffold")
deduction = 1879.52/2852.80
current_rate = 35.66
rent = 1963*12
promised_raise = 1.08
spring = 5
fall  = 4
hours_in_month = 40*52/12
anticipated_raise_winter = 1.06
income_pre_deduction = 40*52*current_rate
income_post_deduction = 40*52*current_rate*deduction
real_income = income_post_deduction - rent
lost_wages_spring = round(current_rate * deduction * (promised_raise-1) * (spring) * hours_in_month)
lost_wages_fall = round(current_rate * deduction * (promised_raise-1) * (spring+fall) * hours_in_month)
bonus = 1000
# print(f'missing out on ${real_income*(promised_raise-1)} a year in spendable dollars')
print(f'monthly real income == ${round(real_income/12)}')
print(f'lost post deduction wages until fall accounting for bonus ${lost_wages_spring-bonus}')
print(f'lost post deduction wages through january accounting for bonus ${lost_wages_fall}')
jace_rate = 35.46
jude_rate = 40.11
print(jude_rate/current_rate)
junior_engineer_wsp = 38
junior_engineer_IH_less_exp = 35.95


class PayStub:

    def __init__(self, date, gross, net):
        self.date = date
        self.gross = gross
        self.net = net

    def __str__(self):
        print(f"On {self.date} I made ${self.gross} gross & ${self.net} net")


class PaySummary:

    def __init__(self, df):
        self.stubs = []
        rawlst = df.values.tolist()
        print(rawlst)
        dates = rawlst[0:len(rawlst)-3:3]
        net = rawlst[1:len(rawlst)-2:3]
        gross = rawlst[2:len(rawlst)-1:3]
        self.visual_df = pd.DataFrame({'dates': dates, 'gross': gross, 'net': net}, columns=['dates', 'gross', 'net'])
        print(self.visual_df)
        for i in range(len(dates)):
            self.stubs.append(PayStub(dates[i], gross[i], net[i]))

    def histogram(self):
        self.visual_df.plot(kind='bar', stacked=True)
        plt.xticks(rotation=30, horizontalalignment="center")
        plt.title("Daniel Farrell Career Compensation Summary")
        plt.xlabel("Date")
        plt.ylabel("Compensation ($)")


October_13 = PaySummary(raw_rates_df)

October_13.histogram()
