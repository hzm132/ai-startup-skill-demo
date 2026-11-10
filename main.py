from dataclasses import dataclass, field
from datetime import date

STEPS = [
    ('validation', '验证', '访谈 10 个目标用户并记录痛点'),
    ('bp', 'BP', '用一页纸写清问题、方案、市场与壁垒'),
    ('policy', '政策', '检查数据合规、版权与行业准入'),
    ('pitch', '路演', '准备 3 分钟 Demo 和 10 页 Deck'),
    ('growth', '获客', '选一个渠道做 7 天低成本投放'),
    ('pricing', '定价', '设计三档价格并访谈付费意愿'),
    ('register', '注册', '确定公司主体、股权与知识产权归属'),
]

@dataclass
class StartupPlan:
    name: str
    done: set = field(default_factory=set)

    def complete(self, key):
        valid = {k for k, _, _ in STEPS}
        if key not in valid:
            raise ValueError(f'未知步骤: {key}')
        self.done.add(key)

    def progress(self):
        return len(self.done), len(STEPS)

    def next_step(self):
        for key, title, task in STEPS:
            if key not in self.done:
                return key, title, task
        return None

    def render(self):
        lines = [f'AI Startup Plan: {self.name} ({date.today()})']
        for key, title, task in STEPS:
            mark = 'x' if key in self.done else ' '
            lines.append(f'[{mark}] {title}: {task}')
        done, total = self.progress()
        lines.append(f'进度: {done}/{total}')
        return '\n'.join(lines)

def main():
    plan = StartupPlan('DemoCo')
    plan.complete('validation')
    plan.complete('bp')
    print(plan.render())
    print()
    print('下一步:', plan.next_step()[1])

if __name__ == '__main__':
    main()