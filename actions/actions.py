from typing import Text, List, Dict

from rasa_sdk import Tracker, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher


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
