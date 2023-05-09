import kivy
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.scatter import Scatter
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.spinner import Spinner
from kivy.config import Config
from kivy.uix.popup import Popup 
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen 
import pandas as pd
import datetime
from kivy.utils import platform
import os
Config.set('graphics', 'resizable', True)
user_inp="0"
class dairyhome(RelativeLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		add_data = Button(size_hint =(.4, .05),pos_hint={"center_x":.5,"center_y":.7},
					text ="Add Data")
		
		#print(period)
		add_data.bind(on_press=self.add_data_screen)
		
		analyze_data = Button(size_hint =(.4, .05),pos_hint={"center_x":.5,"center_y":.6},
					text ="Analyze")
		analyze_data.bind(on_press=self.analyze_data_scrn)
		show_data = Button(size_hint =(.4, .05),pos_hint={"center_x":.5,"center_y":.5},
					text ="Show Data")
		show_data.bind(on_press=self.show_data_scrn)
		clear_data = Button(size_hint =(.4, .05),pos_hint={"center_x":.5,"center_y":.4},
					text ="Clear Data")
		clear_data.bind(on_press=self.cleardata)
		download_data = Button(size_hint =(.4, .05),pos_hint={"center_x":.5,"center_y":.3},
					text ="Download Data")
		download_data.bind(on_press=self.downloaddata)
		self.add_widget(add_data)
		self.add_widget(analyze_data)
		self.add_widget(show_data)
		self.add_widget(clear_data)
		self.add_widget(download_data)
	def downloaddata(self,instance):
		df = pd.read_csv("dairy.csv")
		date = datetime.date.today().strftime('%d-%m-%Y')
		if platform == 'android':
		    from android.storage import primary_external_storage_path
		    dir = primary_external_storage_path()
		    download_dir_path = os.path.join(dir, 'Dairy')+"/dairy"+date+".csv"
		    df.to_csv(download_dir_path,index=False)
		    popup = Popup(title='Downloaded',content=Label(text="Downloaded\nSuccessfully"),size_hint=(None, None), size=(400, 400))
		    popup.open()
	def cleardata(self,instance):
	    box = RelativeLayout()
	    box.add_widget(Label(text = "Are you sure you want to clear data? \n Once deleted cannot be recovered!!!",pos_hint={"center_x":.5,"center_y":.7}))
	    #box1 = BoxLayout(size_hint=(1, .1), height=10, pos_hint={'top': 1, 'left':0})
	    self.popup = Popup(title='Check if Correct', title_size= (30), 
	                  title_align = 'center', content = box,size_hint=(None,None)
	                  , size=(600, 800),
	                  auto_dismiss = True)
	    box.add_widget(Button(text = "YES",  on_press=self.clear_csv,size_hint=(.4, .3),pos_hint={"center_x":.7,"center_y":.3}))
	    box.add_widget(Button(text = "NO",  on_press=self.popup.dismiss,size_hint=(.4, .3),pos_hint={"center_x":.3,"center_y":.3}))
	    
	    self.popup.open()
	def clear_csv(self,instance):
		df = pd.DataFrame(columns = ["Date","Period","Cow FAT","Cow SNF","Cow Liters","Buff FAT","Buff SNF","Buff Liters","Total Cow FAT","Total Cow SNF","Total Buff FAT","Total Buff SNF","Total Cow","Total Buff"])
		df.to_csv("dairy.csv",index=False)
		self.popup.dismiss()
		popup = Popup(title='Cleared',content=Label(text='Deleted Successfully.'),size_hint=(None, None), size=(400, 400))
		popup.open()
	def show_data_scrn(self,instance):
		screen_manager.current="Difference"
	def add_data_screen(self,instance):
		global user_inp
		user_inp = "1"
		screen_manager.current="Data"
	def analyze_data_scrn(self,instance):
		global user_inp
		user_inp = "2"
		screen_manager.current="Data"
class input_page(RelativeLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		layout = BoxLayout(size_hint=(1, .1), height=10, pos_hint={'top': 1, 'left':0})
		layout1 = BoxLayout(size_hint=(1, .2), height=10, pos_hint={'top': 1, 'left':0})
		layout2 = BoxLayout(size_hint=(1, .3), height=10, pos_hint={'top': 1, 'left':0})
		layout3 = BoxLayout(size_hint=(1, .4), height=10, pos_hint={'top': 1, 'left':0})
		layout4 = BoxLayout(size_hint=(1, .5), height=10, pos_hint={'top': 1, 'left':0})
		layout5 = BoxLayout(size_hint=(1, .6), height=10, pos_hint={'top': 1, 'left':0})
		layout6 = BoxLayout(size_hint=(1, .7), height=10, pos_hint={'top': 1, 'left':0})
		layout7 = BoxLayout(size_hint=(1, .8), height=10, pos_hint={'top': 1, 'left':0})
		# creating button 
		# size of button is 20 % by hight and width of layout 
		# position is 'center_x':.7, 'center_y':.5 
		self.date = datetime.date.today().strftime('%d-%m-%Y')

		date_b = Label(size_hint =(3, .5), 
					text ="Date : ") 
		values = [datetime.datetime.today().strftime('%d-%m-%Y')]
		for day in range(1,16):
			date_t = (datetime.datetime.today()-datetime.timedelta(days=day)).strftime('%d-%m-%Y')
			values.append(date_t)
			if date_t[:2]=="01" or date_t[:2]=="16":
				break
		self.spinnerObject = Spinner(text =self.date, values = values)
		self.spinnerObject.size_hint = (9, .5)
		period_b = Label(size_hint =(3, .258), 
					text ="AM / PM : ")
		self.spinnerObjectperiod = Spinner(text = datetime.datetime.today().strftime("%p"), 
             values=((datetime.datetime.today() - datetime.timedelta(hours=12)).strftime('%p'),(datetime.datetime.today() - datetime.timedelta(hours=24)).strftime('%p')),size_hint=(9,.258))
		self.b1 = Label(size_hint =(3, .18),
					text ="Cow FAT : ") 

		self.t1 = TextInput(size_hint =(9, .18),write_tab=False,multiline=False)
		s = Scatter()
		# creating button 
		# size of button is 20 % by hight and 50 % width of layout 
		self.b2 = Label(size_hint =(3, .133), 
					text ="Cow SNF : ") 
		self.t2 = TextInput( size_hint =(9, .133),write_tab=False,multiline=False)
		self.c_literl = Label(size_hint =(3, .105),
					text ="Cow Liters : ") 
		self.c_literi = TextInput( size_hint =(9, .105),write_tab=False,multiline=False)
		self.b3 = Label(size_hint =(3, .09),
					text ="Buff FAT : ") 

		self.t3 = TextInput( size_hint =(9, .09),write_tab=False,multiline=False)
		# creating button 
		# size of button is 20 % by hight and 50 % width of layout 
		self.b4 = Label(size_hint =(3, .075), 
					text ="Buff SNF : ") 
		self.t4 = TextInput( size_hint =(9, .075),write_tab=False,multiline=False)
		self.b_literl = Label(size_hint =(3, .065),
					text ="Buffalo Liters : ") 
		self.b_literi = TextInput( size_hint =(9, .065),write_tab=False,multiline=False)

		home_btn = Button(text="Home",size_hint =(.3, .08),pos_hint={"center_x":.2,"center_y":.1})
		home_btn.bind(on_press=self.home_scrn)

		submit_btn = Button(text="Submit",size_hint =(.3, .08),pos_hint={"center_x":.7,"center_y":.1})
		submit_btn.bind(on_press=self.controller)

		self.add_widget(s)
		layout.add_widget(date_b)
		layout.add_widget(self.spinnerObject)
		layout1.add_widget(period_b)
		layout1.add_widget(self.spinnerObjectperiod)
		layout2.add_widget(self.b1)
		layout2.add_widget(self.t1) 
		layout3.add_widget(self.b2)
		layout3.add_widget(self.t2)
		layout4.add_widget(self.c_literl)
		layout4.add_widget(self.c_literi)
		layout5.add_widget(self.b3)
		layout5.add_widget(self.t3) 
		layout6.add_widget(self.b4)
		layout6.add_widget(self.t4)
		layout7.add_widget(self.b_literl)
		layout7.add_widget(self.b_literi)
		self.add_widget(layout)
		self.add_widget(layout1)
		self.add_widget(layout2)
		self.add_widget(layout3)
		self.add_widget(layout4)
		self.add_widget(layout5)
		self.add_widget(layout6)
		self.add_widget(layout7)
		self.add_widget(home_btn)
		self.add_widget(submit_btn)
	def controller(self,instance):
		global user_inp
		if user_inp=="1":
			date_p = self.spinnerObject.text
			period_p = self.spinnerObjectperiod.text

			try:
				c_fat_p = float(self.t1.text)
				c_snf_p = float(self.t2.text)
				c_lit_p	 = float(self.c_literi.text)
				b_fat_p = float(self.t3.text)
				b_snf_p = float(self.t4.text)
				b_lit_p = float(self.b_literi.text)
				dc_fat_p = 0
				dc_snf_p = 0
				db_fat_p = 0
				db_snf_p = 0
				dc_lit = 0
				db_lit = 0
				
				
				df = pd.read_csv("dairy.csv")
				data = pd.DataFrame({"Date":date_p,"Period":period_p,"Cow FAT":c_fat_p,"Cow SNF":c_snf_p,"Cow Liters":c_lit_p,"Buff FAT":b_fat_p,"Buff SNF":b_snf_p,"Buff Liters":b_lit_p,"Total Cow FAT":dc_fat_p,"Total Cow SNF":dc_snf_p,"Total Buff FAT":db_fat_p,"Total Buff SNF":db_snf_p,"Total Cow":dc_lit,"Total Buff":db_lit},index=[1])
				df = df.append(data,ignore_index=True,sort = False)
				df.to_csv("dairy.csv",index=False)
				screen_manager.current="Saved"
			except Exception as e:
				popup = Popup(title='Text Error',content=Label(text='Please enter correct values.'),size_hint=(None, None), size=(400, 400))
				popup.open()
			self.spinnerObject.text = self.date
			self.spinnerObjectperiod.text = text = datetime.datetime.today().strftime("%p")
			self.t1.text = ""
			self.t2.text = ""
			self.t3.text = ""
			self.t4.text = ""
			self.c_literi.text = ""
			self.b_literi.text = ""
		if user_inp=="2":
			date_p = self.spinnerObject.text
			period_p = self.spinnerObjectperiod.text
			print(date_p)
			f = open("timer.py","w")
			g_time = "g_time = '"+date_p+"'\n"
			g_period = "g_period = '"+period_p+"'"
			f.write(g_time)
			f.write(g_period)
			f.close()
			try:
				c_fat_p = float(self.t1.text)
				c_snf_p = float(self.t2.text)
				c_lit_p	 = float(self.c_literi.text)
				b_fat_p = float(self.t3.text)
				b_snf_p = float(self.t4.text)
				b_lit_p = float(self.b_literi.text)
				
				self.spinnerObject.text = self.date
				self.spinnerObjectperiod.text = text = datetime.datetime.today().strftime("%p")
				self.t1.text = ""
				self.t2.text = ""
				self.t3.text = ""
				self.t4.text = ""
				self.c_literi.text = ""
				self.b_literi.text = ""
				df = pd.read_csv("dairy.csv")
				if date_p in list(df["Date"]):
					if period_p in list(df["Period"]):
						for i in range(len(df)):
							if df.iloc[i][0] == date_p:
								if df.iloc[i][1] == period_p:
									break

					dc_lit = c_lit_p-df.iloc[i][4]
					db_lit = b_lit_p-df.iloc[i][7]
					dc_fat_p = c_fat_p-df.iloc[i][2]
					dc_snf_p = c_snf_p-df.iloc[i][3]
					db_fat_p = b_fat_p-df.iloc[i][5]
					db_snf_p = b_snf_p-df.iloc[i][6]
					data = pd.DataFrame({"Date":date_p,"Period":period_p,"Cow FAT":c_fat_p,"Cow SNF":c_snf_p,"Cow Liters":c_lit_p,"Buff FAT":b_fat_p,"Buff SNF":b_snf_p,"Buff Liters":b_lit_p,"Total Cow FAT":dc_fat_p,"Total Cow SNF":dc_snf_p,"Total Buff FAT":db_fat_p,"Total Buff SNF":db_snf_p,"Total Cow":dc_lit,"Total Buff":db_lit},index=[1])
					df = pd.concat([df.iloc[:i+1], data, df.iloc[i+1:]]).reset_index(drop=True)
					df.to_csv("dairy.csv",index=False)
					screen_manager.current="Difference"
				else:
					popup = Popup(title='Data Not Found',content=Label(text='Data with Date : '+date_p+" "+period_p+"\nis not recorded. Try again with\nanother date or add data."),size_hint=(None, None), size=(400, 400))
					popup.open()
			except Exception as e:
				popup = Popup(title='Text Error',content=Label(text='Please enter correct values.'),size_hint=(None, None), size=(400, 400))
				popup.open()
	def home_scrn(self,instance):
		screen_manager.current="Home"
class save_data(RelativeLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		save_label = Label(size_hint =(1, 1.8),pos_hint={"center_x":.5,"center_y":.5},
					text ="Data Saved Successfully")
		home_btn = Button(text="Home",size_hint =(.3, .08),pos_hint={"center_x":.5,"center_y":.1})
		home_btn.bind(on_press=self.home_scrn)
		self.add_widget(save_label)
		self.add_widget(home_btn)
	def home_scrn(self,instance):
		screen_manager.current="Home"
class analyzed_data(RelativeLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		scroll_layout = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
		layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		layout.bind(minimum_height=layout.setter('height'))
		boxlayout = BoxLayout(size_hint_y=None, height=40)
		boxlayout1 = BoxLayout(size_hint_y=None, height=40)
		date = datetime.date.today().strftime('%d-%m-%Y')
		date_b = Label(text ="Date : ") 
		values = [datetime.date.today().strftime('%d-%m-%Y')]
		for day in range(1,16):
			date_t = (datetime.datetime.today()-datetime.timedelta(days=day)).strftime('%d-%m-%Y')
			values.append(date_t)
			if date_t[:2]=="01" or date_t[:2]=="16":
				break
		self.spinnerObject = Spinner(text =date, values = values)
		period_b = Label(text ="AM / PM : ")
		self.spinnerObjectperiod = Spinner(text = datetime.datetime.today().strftime("%p"), 
             values=("AM","PM"))
		boxlayout.add_widget(date_b)
		boxlayout.add_widget(self.spinnerObject)
		boxlayout1.add_widget(period_b)
		boxlayout1.add_widget(self.spinnerObjectperiod)
		self.cfat_l = Label(text ="Cow FAT : ",size_hint_y=None, height=40)
		self.csnf_l = Label(text ="Cow SNF : ",size_hint_y=None, height=40)
		self.bfat_l = Label(text ="Buffalo FAT : ",size_hint_y=None, height=40)
		self.bsnf_l = Label(text ="Buffalo SNF : ",size_hint_y=None, height=40)
		self.today_cliters_label = Label(text ="Today Cow liters : ",size_hint_y=None, height=40)
		self.today_bliters_label = Label(text ="Today Buffalo liters : ",size_hint_y=None, height=40)
		self.tcfat_l = Label(text ="Total Cow FAT : ",size_hint_y=None, height=40)
		self.tcsnf_l = Label(text ="Total Cow SNF : ",size_hint_y=None, height=40)
		self.tbfat_l = Label(text ="Total Buffalo FAT : ",size_hint_y=None, height=40)
		self.tbsnf_l = Label(text ="Total Buffalo SNF : ",size_hint_y=None, height=40)
		self.empty = Label(text ="",size_hint_y=None, height=40)

		self.total_cliters_label = Label(text ="Total Cow liters : ",size_hint_y=None, height=40)

		self.total_bliters_label = Label(text ="Total Buffalo liters : ",size_hint_y=None, height=40)
		self.submit_scrn()
		layout.add_widget(boxlayout)
		layout.add_widget(boxlayout1)
		layout.add_widget(self.cfat_l)
		layout.add_widget(self.csnf_l)
		layout.add_widget(self.bfat_l)
		layout.add_widget(self.bsnf_l)
		layout.add_widget(self.today_cliters_label)
		layout.add_widget(self.today_bliters_label)
		layout.add_widget(self.empty)
		layout.add_widget(self.tcfat_l)
		layout.add_widget(self.tcsnf_l)
		layout.add_widget(self.tbfat_l)
		layout.add_widget(self.tbsnf_l)
		layout.add_widget(self.total_cliters_label)
		layout.add_widget(self.total_bliters_label)


		
		home_btn = Button(text="Home",size_hint_y=None, height=40)
		home_btn.bind(on_press=self.home_scrn)

		submit_btn = Button(text="Submit",size_hint_y=None, height=40)
		submit_btn.bind(on_press=self.submit_scrn_btn)
		layout.add_widget(submit_btn)
		layout.add_widget(home_btn)
		scroll_layout.add_widget(layout)
		self.add_widget(scroll_layout)
	def submit_scrn_btn(self,instance):
		#g_time = self.spinnerObject.text
		#popup = Popup(title='Data Not Found',content=Label(text='Data with Date : '+date_p+" "+period_p+"\nis not recorded. Try again with\nanother date or add data."),size_hint=(None, None), size=(400, 400))
		#popup.open()
		self.submit_scrn()
	def submit_scrn(self):
		g_time = self.spinnerObject.text
		g_period = self.spinnerObjectperiod.text
		df = pd.read_csv("dairy.csv")
		for i in range(len(df)):
			if df.iloc[i][0] == g_time:
				if df.iloc[i][1] == g_period:
					break
		try:
			dc_fat = (str(df.iloc[i+1][2]-df.iloc[i][2]))[:5]
		except Exception as e:
			dc_fat = "Data Not Found"
		try:
			dc_snf = (str(df.iloc[i+1][3]-df.iloc[i][3]))[:5]
		except Exception as e:
			dc_snf = "Data Not Found"
		try:
			dc_lit = (str(df.iloc[i+1][4]-df.iloc[i][4]))[:5]
		except Exception as e:
			dc_lit = "Data Not Found"
		try:
			db_fat = (str(df.iloc[i+1][5]-df.iloc[i][5]))[:5]
		except Exception as e:
			db_fat = "Data Not Found"
		try:
			db_snf = (str(df.iloc[i+1][6]-df.iloc[i][6]))[:5]
		except Exception as e:
			db_snf = "Data Not Found"
		try:
			db_lit = (str(df.iloc[i+1][7]-df.iloc[i][7]))[:5]
		except Exception as e:
			db_lit = "Data Not Found"
		try:
			tc_diff = (str(df["Total Cow"].sum()))[:5]
		except Exception as e:
			tc_diff = "Data Not Found"
		try:
			tb_diff = (str(df["Total Buff"].sum()))[:5]
		except Exception as e:
			tb_diff = "Data Not Found"
		try:
			tc_fat = (str(df["Total Cow FAT"].sum()))[:5]
		except Exception as e:
			tc_fat = "Data Not Found"
		try:
			tb_fat = (str(df["Total Buff FAT"].sum()))[:5]
		except Exception as e:
			tb_fat = "Data Not Found"
		try:
			tc_snf = (str(df["Total Cow SNF"].sum()))[:5]
		except Exception as e:
			tc_snf = "Data Not Found"
		try:
			tb_snf = (str(df["Total Buff SNF"].sum()))[:5]
		except Exception as e:
			tb_snf = "Data Not Found"
		self.cfat_l.text ="Cow FAT          :  "+dc_fat
		self.csnf_l.text ="Cow SNF          :  "+dc_snf
		self.bfat_l.text ="Buffalo FAT      :  "+db_fat
		self.bsnf_l.text ="Buffalo SNF      :  "+db_snf
		self.today_cliters_label.text ="Today Cow liters     :  "+dc_lit
		self.today_bliters_label.text ="Today Buffalo liters :  "+db_lit
		self.total_cliters_label.text ="Total Cow liters     :  "+tc_diff
		self.total_bliters_label.text ="Total Buffalo liters :  "+tb_diff
		self.tcfat_l.text = "Total Cow FAT      :  "+tc_fat
		self.tcsnf_l.text = "Total Cow SNF      :  "+tc_snf
		self.tbfat_l.text = "Total Buffalo FAT  :  "+tb_fat
		self.tbsnf_l.text = "Total Buffalo SNF  :  "+tb_snf
		
	def home_scrn(self,instance):
		screen_manager.current="Home"
class DairyApp(App):
	def build(self):
		#self.screen_manager = ScreenManager()
		time = datetime.date.today().strftime('%d-%m-%Y')
		period = datetime.datetime.today().strftime("%p")
		self.home_page = dairyhome()
		screen = Screen(name='Home')
		screen.add_widget(self.home_page)
		screen_manager.add_widget(screen)
		self.page_input=input_page()
		screen = Screen(name='Data')
		screen.add_widget(self.page_input)
		screen_manager.add_widget(screen)
		self.data_add=save_data()
		screen = Screen(name='Saved')
		screen.add_widget(self.data_add)
		screen_manager.add_widget(screen)
		self.analyzed=analyzed_data()
		screen = Screen(name='Difference')
		screen.add_widget(self.analyzed)
		screen_manager.add_widget(screen)
		return screen_manager

	
screen_manager = ScreenManager()
if __name__ == "__main__":
    dairy_app = DairyApp().run()