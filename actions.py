import requests
import json
import openweathermapy.core as owm
import json 

from api_keys import api_key
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
# from citipy import citipy

class Actionviva(Action):
    def name(self) -> Text:
        return "action_viva"
    
    def run(self,dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text,Any]) -> List[Dict[Text, Any]]:

        dance = tracker.get_slot("dance_type")
        informa = "mondays at 7"
        dispatcher.utter_message(f"this is the viva chatbot{dance}")
        return [SlotSet("class_info", informa)]
# class findWeather():
#     def __init__(self):
#         # self.city = input("in what city are you located?")
#         self.city = 'default'
        
        
#     def wea(self):
#         # self.city = input("in what city are you located?")  
#         settings = {'units':'metric','appid':api_key}
#         cities_weather=[]
#         # city = input("in what city are you located?")

#         try:
#             cities_weather.append(owm.get_current(self.city,**settings))
#             print(f"Processing record | {self.city}")
#         except:
#         #         if err.code == 404:
#             print(f'City {self.city} not found... Skipping')

#         # this is the information we are looking for, we will create a summery list that we are going to use with the wrapper
#         summary = ['name','clouds.all','sys.country','main.humidity','coord.lat','coord.lon',
#                 'main.temp_max','wind.speed']
#         data = [cities_weather[0](*summary)]

#         data_dict = {"City": data[0][0],
#                     "Cloudiness": data[0][1],
#                     "Country": data[0][2],
#                     "Humidity": data[0][3],
#                     "Lat": data[0][4],
#                     "Lon": data[0][5],
#                     "Max": data[0][6],
#                     "Min": data[0][7]}
#         # print (data)
#         # print (data_dict)

#         return data_dict

def _theweather(city):
    # self.city = input("in what city are you located?")
        
    settings = {'units':'metric','appid':api_key}
    cities_weather=[]
    # city = input("in what city are you located?")

    try:
        cities_weather.append(owm.get_current(city,**settings))
        print(f"Processing record | {city}")
    except:
    #         if err.code == 404:
        print(f'City {city} not found... Skipping')

    # this is the information we are looking for, we will create a summery list that we are going to use with the wrapper
    summary = ['name','clouds.all','sys.country','main.humidity','coord.lat','coord.lon',
            'main.temp_max','wind.speed']
    data = [cities_weather[0](*summary)]

    data_dict = {"City": data[0][0],
                "Cloudiness": data[0][1],
                "Country": data[0][2],
                "Humidity": data[0][3],
                "Lat": data[0][4],
                "Lon": data[0][5],
                "Max": data[0][6],
                "Min": data[0][7]}
    # print (data)
    # print (data_dict)

    return data_dict
# xx = findWeather().wea
# print(findWeather())
# xx = findWeather()

class weatherForm(FormAction):
    def name(self) -> Text:
        return "weather_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]: # , dispatcher: CollectingDispatcher
        # print('we got to the required slots')
        # if tracker.get_slot('location') is None:
        #     print('we got here')
        #     # dispatcher.utter_message("please provide location") 
        #     return["dance_type", "classes_type"]
        # else:
        return["dance_type", "class_type", "location"]
    def slot_mappings(self):

        return{
            "dance_type": self.from_entity(entity='dance_type', intent= "class_schedule_ques"),
            "class_type": self.from_entity(entity="class_type", intent= "class_schedule_ques"),
            "location": self.from_entity(entity="location", intent= "loc_info")}



    # @staticmethod
    # def request_next_slot(
    #     self,
    #     dispatcher: "CollectingDispatcher",
    #     tracker: "Tracker",
    #     domain: Dict[Text, Any],
    # ):

    #     """Request the next slot and utter template if needed,
    #         else return None"""
    #     for slot in self.required_slots(tracker):
    #         if self._should_request_slot(tracker, slot):

    #             ## Condition of validated slot that triggers deactivation
    #             if slot == "location" and tracker.get_slot("location") == None:
    #                 the_slot = slot
    #                 dispatcher.utter_message(text=f"Sorry, I can't help you with that please provide{the_slot} ")
    #                 return self.deactivate()

    #             ## For all other slots, continue as usual
    #             logger.debug(f"Request next slot '{slot}'")
    #             dispatcher.utter_message(
    #                 template=f"utter_ask_{slot}", **tracker.slots
    #             )
    #             return [SlotSet(REQUESTED_SLOT, slot)]
    #     return None
    # def validate_location(
    #     self,
    #     value: Text,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> Dict[Text, Any]:
    #     """Validate cuisine value."""

    #     if value.lower() in self.cuisine_db():
    #         # validation succeeded, set the value of the "cuisine" slot to value
    #         return {"cuisine": value}
    #     else:
    #         dispatcher.utter_message(template="utter_wrong_cuisine")
    #         # validation failed, set this slot to None, meaning the
    #         # user will be asked for the slot again
    #         return {"cuisine": None}


    def submit(self, 
                dispatcher: CollectingDispatcher,
                tracker: Tracker,
                domain: Dict[Text, Any]) -> List[Dict]:
        print('the form has got to this point in the submit')
        location = tracker.get_slot('location')
        class_type = tracker.get_slot('class_type')
        dance = tracker.get_slot('dance_type')

        results = _theweather(location)

        if len(results) == 0:
            dispatcher.utter_message(f"sorry we could not find {location} ")

            return []
        if dance == 'salsa':
            dispatcher.utter_message(f"Salsa classes are offered Wednesdays at 7:00 pm")
        elif dance == 'bachata':
            dispatcher.utter_message(f"Bachata classes are offered every Monday at 7:00 pm")
        dispatcher.utter_message(f"The weather is {results}")

        return []











# settings = {'units':'metric','appid':api_key}
# cities_weather=[]
# city = input("in what city are you located?")

# try:
#     cities_weather.append(owm.get_current(city,**settings))
#     print(f"Processing record | {city}")
# except:
# #         if err.code == 404:
#     print(f'City {city} not found... Skipping')

# # this is the information we are looking for, we will create a summery list that we are going to use with the wrapper
# summary = ['name','clouds.all','sys.country','main.humidity','coord.lat','coord.lon',
#           'main.temp_max','wind.speed']
# data = [cities_weather[0](*summary)]

# data_dict = {"City": data[0][0],
#             "Cloudiness": data[0][1],
#             "Country": data[0][2],
#             "Humidity": data[0][3],
#             "Lat": data[0][4],
#             "Lon": data[0][5],
#             "Max": data[0][6],
#             "Min": data[0][7]}
# print (data)
# print (data_dict)