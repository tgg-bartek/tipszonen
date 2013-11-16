from django.db import models
from django.contrib.auth.models import User 
from django.template.defaultfilters import slugify


class Pick(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    matchup = models.CharField(max_length=255, help_text='''Ex: Fc Barcelona vs 
        Real Mardit''')
    slug = models.SlugField(max_length=255, blank=True, default='', help_text='''
            Populates automatically. It's advisable you do not change it.''')
    match_date = models.DateTimeField()
    selection = models.CharField('your pick', max_length=128)
    one_unit = 1
    two_unit = 2
    three_unit = 3
    UNIT_CHOICES = (
        (one_unit, 1),
        (two_unit, 2),
        (three_unit, 3),
    )
    stake = models.IntegerField(choices=UNIT_CHOICES, default=one_unit)

    pinna = 'Pinnacle'
    sbo = 'SBO'
    bet_188 = '188bet'
    bet365 = 'bet365'
    BOOKIE_CHOICES = (
        (pinna, 'Pinnacle'),
        (sbo, 'SBO'),
        (bet_188, '188bet'),
        (bet365, 'bet365'),
    )
    bookmaker = models.CharField(max_length=30, choices=BOOKIE_CHOICES,
                                                         default=pinna)

    odds = models.FloatField(help_text='''Use decimal odds. When floating point,
            put a dot (.) Ex: 1.75''')
    analysis = models.TextField(blank=True, help_text='''Consider adding
            competition info, ex: Football - Sweden - Allsvenskan''')
    published = models.BooleanField(default=True) 
    expert = models.ForeignKey('picks.ExpertCategory')

    match_score = models.CharField(max_length=20, help_text='Ex: 3-0', blank=True)

    not_started = '?'
    win = '1'
    half_win = '0.5'
    push = '0'
    half_loss = '-0.5'
    loss = '-1'
    OUTCOME_CHOICES = (
        (not_started, '?'),
        (win, 'win'),
        (half_win, '1/2 win'),
        (push, 'push'),
        (half_loss, '1/2 loss'),
        (loss, 'loss'),
    )
    pick_outcome = models.CharField(max_length=20, choices=OUTCOME_CHOICES, 
                                                    default=not_started)

    class Meta:
        ordering = ['-created_at', 'matchup']

    def __unicode__(self):
        return self.matchup 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Pick, self).save(*args, **kwargs)

    def calculate_profit(self):
        self.odds = float(self.odds) 
        if self.pick_outcome != '?':
            self.pick_outcome = float(self.pick_outcome)
            if self.pick_outcome <= 0: # loss or push
                return '{:0.2f}'.format(self.pick_outcome * self.stake) 
            return '{:0.2f}'.format((self.pick_outcome * self.stake * 
                        self.odds) - (self.stake * self.pick_outcome))
        return self.pick_outcome  # `?`


class ExpertCategory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ['-name']
        verbose_name_plural = 'ExpertCategories'

    def __unicode__(self):
        return self.name 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(ExpertCategory, self).save(*args, **kwargs)

