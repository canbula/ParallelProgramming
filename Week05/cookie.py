import asyncio
import time
import logging


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
        self.__chef_is_busy = False
        self.__mix_the_dry_ingredients = False
        self.__allow_ingredients_to_reach_room_temperature = False
        self.__mix_the_wet_ingredients = False
        self.__combine_the_dry_and_wet_ingredients = False
        self.__add_chocolate_chips = False
        self.__chill_the_dough = False
        self.__roll_the_dough_into_balls = False
        self.__preheat_the_oven = False
        self.__bake_the_cookies = False

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
        if not self.__bake_the_cookies:
            logging.error("The cookies are not baked")
        logging.info(f"It took {((self.__end_time - self.__start_time)/self._minute):.2f} "
                     f"minutes to complete this recipe.")
        return True

    async def mix_the_dry_ingredients(self) -> None:
        """
        Mix the flour, baking soda, and salt in a large bowl.

        Time: 2 minutes
        Requires: None
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Mixing the dry ingredients")
        await asyncio.sleep(2 * self._minute)
        logging.info("[END] Mixing the dry ingredients")
        self.__chef_is_busy = False
        self.__mix_the_dry_ingredients = True
        return None

    async def allow_ingredients_to_reach_room_temperature(self) -> None:
        """
        Allow the butter and egg to reach room temperature.

        Time: 10 minutes
        Requires: None
        Occupies Chef: No
        """
        logging.info("[START] Allowing the ingredients to reach room temperature")
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] Allowing the ingredients to reach room temperature")
        self.__allow_ingredients_to_reach_room_temperature = True
        return None

    async def mix_the_wet_ingredients(self) -> None:
        """
        Mix the butter (at room temperature), sugar, brown sugar,
        egg (at room temperature), and vanilla in a bowl.

        Time: 3 minutes
        Requires: Butter and egg at room temperature
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        if not self.__allow_ingredients_to_reach_room_temperature:
            logging.error("The butter and egg are not at room temperature")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Mixing the wet ingredients")
        await asyncio.sleep(3 * self._minute)
        logging.info("[END] Mixing the wet ingredients")
        self.__chef_is_busy = False
        self.__mix_the_wet_ingredients = True
        return None

    async def combine_the_dry_and_wet_ingredients(self) -> None:
        """
        Combine the dry and wet ingredients.

        Time: 5 minutes
        Requires: Mixed dry ingredients and mixed wet ingredients
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        if not self.__mix_the_dry_ingredients:
            logging.error("The dry ingredients are not mixed")
            return None
        if not self.__mix_the_wet_ingredients:
            logging.error("The wet ingredients are not mixed")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Combining the dry and wet ingredients")
        await asyncio.sleep(5 * self._minute)
        logging.info("[END] Combining the dry and wet ingredients")
        self.__chef_is_busy = False
        self.__combine_the_dry_and_wet_ingredients = True
        return None

    async def add_chocolate_chips(self) -> None:
        """
        Add the chocolate chips.

        Time: 1 minute
        Requires: Combined dry and wet ingredients
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        if not self.__combine_the_dry_and_wet_ingredients:
            logging.error("The dry and wet ingredients are not combined")
            return None
        self.__chef_is_busy = True
        logging.info("[START] Adding the chocolate chips")
        await asyncio.sleep(1 * self._minute)
        logging.info("[END] Adding the chocolate chips")
        self.__chef_is_busy = False
        self.__add_chocolate_chips = True
        return None

    async def chill_the_dough(self) -> None:
        """
        Chill the dough.

        Time: 60 minutes
        Requires: Added chocolate chips
        Occupies Chef: No
        """
        if not self.__add_chocolate_chips:
            logging.error("The chocolate chips are not added")
            return None
        logging.info("[START] Chilling the dough")
        await asyncio.sleep(60 * self._minute)
        logging.info("[END] Chilling the dough")
        self.__chill_the_dough = True
        return None

    async def roll_the_dough_into_balls(self) -> None:
        """
        Roll the dough into balls.

        Time: 10 minutes
        Requires: Chilled dough
        Occupies Chef: Yes
        """
        if self.__chef_is_busy:
            logging.error("The chef is busy")
            return None
        if not self.__chill_the_dough:
            logging.error("The dough is not chilled")
            return None
        logging.info("[START] Rolling the dough into balls")
        await asyncio.sleep(10 * self._minute)
        logging.info("[END] Rolling the dough into balls")
        self.__roll_the_dough_into_balls = True
        return None

    async def preheat_the_oven(self) -> None:
        """
        Preheat the oven.

        Time: 15 minutes
        Requires: None
        Occupies Chef: No
        """
        logging.info("[START] Preheating the oven")
        await asyncio.sleep(15 * self._minute)
        logging.info("[END] Preheating the oven")
        self.__preheat_the_oven = True
        return None

    async def bake_the_cookies(self) -> None:
        """
        Bake the cookies.

        Time: 15 minutes
        Requires: Rolled dough into balls and preheated oven
        Occupies Chef: No
        """
        if not self.__roll_the_dough_into_balls:
            logging.error("The dough is not rolled into balls")
            return None
        if not self.__preheat_the_oven:
            logging.error("The oven is not preheated")
            return None
        logging.info("[START] Baking the cookies")
        await asyncio.sleep(15 * self._minute)
        logging.info("[END] Baking the cookies")
        self.__bake_the_cookies = True
        return None

    @property
    def minute(self):
        return self._minute


async def main_run() -> None:
    async with ChocolateChipCookie(0.1) as cookie:
        await cookie.mix_the_dry_ingredients()
        await cookie.allow_ingredients_to_reach_room_temperature()
        await cookie.mix_the_wet_ingredients()
        await cookie.combine_the_dry_and_wet_ingredients()
        await cookie.add_chocolate_chips()
        await cookie.chill_the_dough()
        await cookie.roll_the_dough_into_balls()
        await cookie.preheat_the_oven()
        await cookie.bake_the_cookies()
    return None


async def main_wait_for() -> None:
    async with ChocolateChipCookie(0.1) as cookie:
        await asyncio.wait_for(cookie.mix_the_dry_ingredients(), None)
        await asyncio.wait_for(cookie.allow_ingredients_to_reach_room_temperature(), None)
        await asyncio.wait_for(cookie.mix_the_wet_ingredients(), None)
        await asyncio.wait_for(cookie.combine_the_dry_and_wet_ingredients(), None)
        await asyncio.wait_for(cookie.add_chocolate_chips(), None)
        await asyncio.wait_for(cookie.chill_the_dough(), None)
        await asyncio.wait_for(cookie.roll_the_dough_into_balls(), None)
        await asyncio.wait_for(cookie.preheat_the_oven(), None)
        await asyncio.wait_for(cookie.bake_the_cookies(), None)
    return None


async def main_gather() -> None:
    async with ChocolateChipCookie(0.1) as cookie:
        await asyncio.gather(
            cookie.mix_the_dry_ingredients(),
            cookie.allow_ingredients_to_reach_room_temperature(),
            cookie.mix_the_wet_ingredients(),
            cookie.combine_the_dry_and_wet_ingredients(),
            cookie.add_chocolate_chips(),
            cookie.chill_the_dough(),
            cookie.roll_the_dough_into_balls(),
            cookie.preheat_the_oven(),
            cookie.bake_the_cookies(),
        )
    return None


async def main() -> None:
    async with ChocolateChipCookie(0.1) as cookie:
        task_1 = [
            cookie.mix_the_dry_ingredients(),
            cookie.allow_ingredients_to_reach_room_temperature()
        ]
        await asyncio.gather(*task_1)
        await cookie.mix_the_wet_ingredients()
        await cookie.combine_the_dry_and_wet_ingredients()
        await cookie.add_chocolate_chips()
        task_2 = [
            cookie.chill_the_dough(),
            cookie.preheat_the_oven()
        ]
        await asyncio.gather(*task_2)
        await cookie.roll_the_dough_into_balls()
        await cookie.bake_the_cookies()
    return None


if __name__ == '__main__':
    asyncio.run(main())
