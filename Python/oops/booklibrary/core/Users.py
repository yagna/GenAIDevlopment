from abc import ABC, abstractmethod

class Person(ABC):
    """Abstract base class representing a person who can borrow and return items."""

    @abstractmethod
    def borrow_item(self):
        """Borrow an item.

        This method should define how the person borrows an item.
        Implementations might include updating an inventory, logging
        the transaction, or tracking due dates.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        pass

    @abstractmethod
    def return_item(self):
        """Return an item.

        This method should define how the person returns an item.
        Implementations might include updating an inventory or marking
        the item as returned.

        Raises:
            NotImplementedError: If the subclass does not implement this method.
        """
        pass
