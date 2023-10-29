from typing import Text, List, Dict, Any

from rasa_sdk import Tracker, Action, ValidationAction
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher


# Actions for formatting yes/no buttons

class AskForOutsideSitsAction(Action):
    def name(self) -> Text:
        return "action_ask_has_outside_sits"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text="Would you like to sit outside?",
            buttons=[
                {"title": "yes", "payload": "/affirm"},
                {"title": "no", "payload": "/deny"},
            ],
        )
        return []


class AskForIsOpenAction(Action):
    def name(self) -> Text:
        return "action_ask_is_open_now"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        dispatcher.utter_message(
            text="Do you need to search coffee shops that are open now?",
            buttons=[
                {"title": "yes", "payload": "/affirm"},
                {"title": "no", "payload": "/deny"},
            ],
        )
        return []


# Actions for location processing

# Mock-request for getting location's coordinates
def mock_geo(location: str):
    return 54, 34


class ValidateLocationSlots(ValidationAction):
    def validate_location(
            self,
            slot_value: List,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        try:
            # Get the latitude and longitude of the address by geocoding using geopy Nominatim
            latitude, longitude = mock_geo(', '.join(slot_value))

            if latitude is None:
                # If the location isn't recognized then send the following message and set the slot value to none
                dispatcher.utter_message(template="utter_wrong_address")
                return {"location": None}
            else:
                # Otherwise keep the address slot value. Additionally, save the value of the coordinates to slot
                return {"location": slot_value, 'coords': f'{latitude}, {longitude}'}
        except:
            # todo: define exception
            # In case we run into an error we return the following message
            dispatcher.utter_message(text='Facing server issues. Please try again later')
