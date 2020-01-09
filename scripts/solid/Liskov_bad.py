class Event:
    def meets_condition(self, event_data: dict) -> bool:
        return False

class LoginEvent(Event):
    def meets_condition(self, event_data: list) -> bool:
        return bool(event_data)

#mypy error: Argument 1 of "meets_condition" incompatible with supertype "Event"
