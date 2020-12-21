class MotionDimension():
    def __init__(self, pos=0, vel=0, acc=0, max_pos=None, min_pos=None, max_vel=None, min_vel=None):
        self.pos = pos
        self.vel = vel
        self.acc = acc
        self.pos = pos
        self.max_pos = max_pos
        self.min_pos = min_pos
        self.vel = vel
        self.max_vel = max_vel
        self.min_vel = min_vel

    def tick(self):
        self.pos += self.vel
        if self.max_pos is not None and self.pos > self.max_pos:
            self.pos = self.max_pos
        if self.min_pos is not None and self.pos < self.min_pos:
            self.pos = self.min_pos
        self.vel += self.acc
        if self.max_vel is not None and self.vel > self.max_vel:
            self.vel = self.max_vel
        if self.min_vel is not None and self.vel < self.min_vel:
            self.vel = self.min_vel