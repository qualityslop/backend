from __future__ import annotations

import typing as t
from enum import StrEnum

if t.TYPE_CHECKING:
    from qs.game.session import Session


class Occupation(StrEnum):
    SOFTWARE_ENGINEER = "software_engineer"


SALARIES = {
    Occupation.SOFTWARE_ENGINEER: 5000,
}


def get_monthly_salary(occupation: Occupation) -> int:
    return SALARIES[occupation]


class Player:
    def __init__(
        self,
        session: Session,
        username: str,
        is_leader: bool = False,
    ):
        self._session = session
        self._username = username
        self._is_leader = is_leader
        self._balance = 50000
        self._occupation = Occupation.SOFTWARE_ENGINEER
        self._monthly_grocery_expense = 300
        self._monthly_leisure_expense = 250


    def get_session(self) -> Session:
        return self._session


    def get_username(self) -> str:
        return self._username
    

    def is_leader(self) -> bool:
        return self._is_leader
    

    def get_balance(self) -> float:
        return self._balance


    def get_monthly_income(self) -> float:
        return self.get_monthly_salary()
    

    def get_monthly_expenses(self) -> float:
        return (
            self.get_monthly_rent_expense() +
            self.get_monthly_utilities_expense() +
            self.get_monthly_grocery_expense() +
            self.get_monthly_transportation_expense() +
            self.get_monthly_leisure_expense() +
            self.get_monthly_loan_expense() +
            self.get_monthly_tax_expense()
        )


    def get_monthly_net_income(self) -> float:
        return self.get_monthly_income() - self.get_monthly_expenses()
    

    def get_occupation(self) -> Occupation:
        return self._occupation
    

    def get_monthly_salary(self) -> float:
        return get_monthly_salary(self._occupation)


    def get_health_level(self) -> int:
        return 100
    

    def get_happiness_level(self) -> int:
        return 100
    

    def get_energy_level(self) -> int:
        return 100
    

    def get_social_life_level(self) -> int:
        return 100
    

    def get_stress_level(self) -> int:
        return 100
    

    def get_living_comfort_level(self) -> int:
        return 100
    

    def get_monthly_rent_expense(self) -> float:
        return 1000
    

    def get_monthly_utilities_expense(self) -> float:
        return 200
    

    def get_monthly_grocery_expense(self) -> float:
        return self._monthly_grocery_expense
    

    def set_monthly_grocery_expense(self, amount: float) -> None:
        self._monthly_grocery_expense = amount
    

    def get_monthly_transportation_expense(self) -> float:
        return 150
    

    def get_monthly_leisure_expense(self) -> float:
        return self._monthly_leisure_expense
    

    def set_monthly_leisure_expense(self, amount: float) -> None:
        self._monthly_leisure_expense = amount
    

    def get_monthly_loan_expense(self) -> float:
        return 400
    

    def get_monthly_tax_expense(self) -> float:
        return 500


    def buy_meal(self) -> None:
        """Buy a meal. Players eat three times a day."""
        self._balance -= self.get_monthly_grocery_expense() * 4 / 365


    def pay_daily_transportation(self) -> None:
        """Pay for daily transportation."""
        self._balance -= self.get_monthly_transportation_expense() * 12 / 365


    def pay_daily_leisure(self) -> None:
        """Pay for daily leisure."""
        self._balance -= self.get_monthly_leisure_expense() * 12 / 365


    def pay_taxes(self) -> None:
        """Pay the monthly tax expense."""
        self._balance -= self.get_monthly_tax_expense()


    def pay_rent(self) -> None:
        """Pay the monthly rent expense."""
        self._balance -= self.get_monthly_rent_expense()


    def pay_utilities(self) -> None:
        """Pay the monthly utilities expense."""
        self._balance -= self.get_monthly_utilities_expense()

    
    def pay_loan_installment(self) -> None:
        """Pay the monthly loan installment."""
        self._balance -= self.get_monthly_loan_expense()


    def tick(self) -> None:
        time = self._session.get_time()

        if time.day == 1 and time.hour == 0:
            self._balance += self.get_monthly_salary()
            self._balance -= self.get_monthly_rent_expense()
            self._balance -= self.get_monthly_utilities_expense()
            self._balance -= self.get_monthly_loan_expense()
            self._balance -= self.get_monthly_tax_expense()

        if time.hour in (6, 12, 18):
            self.buy_meal()

        if time.hour == 0:
            self.pay_daily_transportation()
            self.pay_daily_leisure()
