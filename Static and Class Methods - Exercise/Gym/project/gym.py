from project import Customer
from project import Equipment
from project import ExercisePlan
from project import Subscription
from project import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next(filter(lambda s: s.id == subscription_id, self.subscriptions))
        customer = next(filter(lambda c: c.id == subscription_id, self.customers))
        trainer = next(filter(lambda t: t.id == subscription_id, self.trainers))
        equipment = next(filter(lambda e: e.id == subscription_id, self.equipment))
        plan = next(filter(lambda p: p.id == subscription_id, self.plans))

        return (
            f"{subscription}\n"
            f"{customer}\n"
            f"{trainer}\n"
            f"{equipment}\n"
            f"{plan}"
        )