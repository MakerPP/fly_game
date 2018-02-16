#跟踪游戏的统计信息

class GameStats():
    def __init__(self,ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """初始化在游戏运行时期可能变化的信息"""
        self.ships_left = self.ai_settings.ship_limit
