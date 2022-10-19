import asyncio
import time
import logging


class CompletedTaskError(Exception):
    pass


class RequiredTaskError(Exception):
    pass


class ChefOccupiedError(Exception):
    pass


class ChocolateChipCookie:
    """
    This class is extracted from Classic
    Chocolate Chip Cookies recipe
    from https://youtu.be/loqCY9b7aec

    STEPS:
    1. [ 2 Minutes] Mix the flour, baking soda, and salt in a large bowl.
    2. [10 Minutes] Allow the butter and egg to reach room temperature.
    3. [ 3 Minutes] Mix the butter (at room temperature), sugar, brown sugar,
                    egg (at room temperature), and vanilla in a bowl.
    4. [ 5 Minutes] Combine the dry and wet ingredients.
    5. [ 1 Minute ] Add the chocolate chips.
    6. [60 Minutes] Chill the dough.
    7. [10 Minutes] Roll the dough into balls.
    8. [15 Minutes] Preheat the oven.
    9. [15 Minutes] Bake the cookies.
    """

    def __init__(self, minute: float = 1.0):
        self._minute = minute
        self.__start_time = time.time()
        self.__end_time = None
        self.__chef_is_available = True
        self.__tasks = {
            "mix_the_dry_ingredients": {
                "name": "Mix the dry ingredients",
                "time": 2,
                "occupies_chef": True,
                "requires": [],
                "completed": False
            },
            "allow_ingredients_to_reach_room_temperature": {
                "name": "Allow the butter and egg to reach room temperature",
                "time": 10,
                "occupies_chef": False,
                "requires": [],
                "completed": False
            },
            "mix_the_wet_ingredients": {
                "name": "Mix the butter (at room temperature), sugar, brown sugar, "
                        "egg (at room temperature), and vanilla in a bowl",
                "time": 3,
                "occupies_chef": True,
                "requires": ["allow_ingredients_to_reach_room_temperature"],
                "completed": False
            },
            "combine_the_dry_and_wet_ingredients": {
                "name": "Combine the dry and wet ingredients",
                "time": 5,
                "occupies_chef": True,
                "requires": ["mix_the_dry_ingredients", "mix_the_wet_ingredients"],
                "completed": False
            },
            "add_chocolate_chips": {
                "name": "Add the chocolate chips",
                "time": 1,
                "occupies_chef": True,
                "requires": ["combine_the_dry_and_wet_ingredients"],
                "completed": False
            },
            "chill_the_dough": {
                "name": "Chill the dough",
                "time": 60,
                "occupies_chef": False,
                "requires": ["add_chocolate_chips"],
                "completed": False
            },
            "roll_the_dough_into_balls": {
                "name": "Roll the dough into balls",
                "time": 10,
                "occupies_chef": True,
                "requires": ["chill_the_dough"],
                "completed": False
            },
            "preheat_the_oven": {
                "name": "Preheat the oven",
                "time": 15,
                "occupies_chef": False,
                "requires": [],
                "completed": False
            },
            "bake_the_cookies": {
                "name": "Bake the cookies",
                "time": 15,
                "occupies_chef": False,
                "requires": ["roll_the_dough_into_balls", "preheat_the_oven"],
                "completed": False
            }
        }

    async def __aenter__(self):
        logging.basicConfig(format='%(levelname)s @ %(asctime)s : %(message)s',
                            datefmt='%d.%m.%Y %H:%M:%S',
                            level=logging.INFO,
                            force=True,
                            handlers=[
                                logging.FileHandler("cookie.log", mode='w'),
                                logging.StreamHandler()
                            ])
        logging.getLogger("asyncio").setLevel(logging.WARNING)
        logging.info("[START] Classic Chocolate Chip Cookies")
        await asyncio.sleep(0)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self.__end_time = time.time()
        await asyncio.sleep(0)
        logging.info("[END] Classic Chocolate Chip Cookies")
        if not self.__tasks["bake_the_cookies"]["completed"]:
            logging.error("The cookies are not baked")
        logging.info(f"It took {((self.__end_time - self.__start_time)/self._minute):.2f} "
                     f"minutes to complete this recipe.")
        return True

    async def __call__(self, task: str) -> None:
        try:
            if self.__tasks[task]["completed"]:
                raise CompletedTaskError
            if not all([self.__tasks[_]["completed"] for _ in self.__tasks[task]["requires"]]):
                raise RequiredTaskError
            if self.__tasks[task]["occupies_chef"]:
                if not self.__chef_is_available:
                    raise ChefOccupiedError
                self.__chef_is_available = False
            logging.info(f"[START] {task}")
            await asyncio.sleep(self.__tasks[task]["time"] * self._minute)
            self.__tasks[task]["completed"] = True
            logging.info(f"[END] {task}")
        except CompletedTaskError:
            logging.warning(f"Task {task} is already completed")
            await asyncio.sleep(0)
            return None
        except RequiredTaskError:
            logging.warning(f"Task {task} is not ready to be completed")
            await asyncio.sleep(0)
            return None
        except ChefOccupiedError:
            logging.warning(f"The chef is not available for {task}")
            await asyncio.sleep(0)
            return None
        finally:
            if self.__tasks[task]["occupies_chef"]:
                self.__chef_is_available = True
            return None


async def main() -> None:
    async with ChocolateChipCookie(0.1) as cookie:
        tasks = [
            ["mix_the_dry_ingredients", "allow_ingredients_to_reach_room_temperature"],
            ["mix_the_wet_ingredients"],
            ["combine_the_dry_and_wet_ingredients"],
            ["add_chocolate_chips"],
            ["chill_the_dough", "preheat_the_oven"],
            ["roll_the_dough_into_balls"],
            ["bake_the_cookies"]
        ]
        for task in tasks:
            await asyncio.gather(*[cookie(t) for t in task])
    return None


if __name__ == '__main__':
    asyncio.run(main())
