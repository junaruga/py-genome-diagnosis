from django.db import models


class Snp(models.Model):
    name = models.CharField(max_length=32)
    # 1, .. , 22, X, Y, MT(Mitochondrion)
    chromosome = models.CharField(max_length=2)
    chromosome_position = models.IntegerField()


class Disease(models.Model):
    disease_id = models.IntegerField()
    name = models.CharField(max_length=128)


class SnpDisease(models.Model):
    snp_name = models.CharField(max_length=32)
    disease_id = models.IntegerField()
    rate = models.DecimalField(max_digits=12, decimal_places=2)


class Genome(models.Model):
    # profile_id: 1 => Ideal human genome reserved by system.
    profile_id = models.IntegerField()
    genome = models.TextField()
