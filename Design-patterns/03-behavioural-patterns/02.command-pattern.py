from __future__ import annotations
from abc import ABC, abstractmethod


class Command(ABC):
    def __init__(self, command_id: int):
        self.command_id = command_id
    
    @abstractmethod
    def execute(self):
        pass

class GetOrderDetails(Command):
    def execute(self):
        print(f"Get Order details for {self.command_id} order id")

class OrderPayment(Command):
    def execute(self):
        print(f"Performing order payment for {self.command_id} order id")

class CommandProcessor:
    queue = []
    
    def add_command(self, command: Command):
        self.queue.append(command)
    
    def process_commands(self):
        [command.execute() for command in self.queue]
        self.queue = []

if __name__ == "__main__":
    processor = CommandProcessor()
    processor.add_command(GetOrderDetails(1))
    processor.add_command(GetOrderDetails(2))
    processor.add_command(GetOrderDetails(3))
    processor.add_command(OrderPayment(1))
    processor.add_command(OrderPayment(3))

    processor.process_commands()
        

