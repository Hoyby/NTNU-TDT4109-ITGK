#!/usr/bin/env python
# coding: utf-8

# <nav class="navbar navbar-default">
#   <div class="container-fluid">
#     <div class="navbar-header">
#       <a class="navbar-brand" href="_Oving3.ipynb">Øving 3</a>
#     </div>
#     <ul class="nav navbar-nav">
#       <li ><a href="Intro%20til%20lokker.ipynb">Intro til løkker</a></li>
#     <li ><a href="Mer%20om%20lokker.ipynb">Mer om løkker</a></li>
#     <li><a href="Nostede%20lokker.ipynb">Intro til nøstede løkker</a></li>
#     <li class="active"><a href="Kodeforstaelse.ipynb">Kodeforståelse</a></li>
#     <li ><a href="Gjett%20tallet.ipynb">Gjett tallet</a></li>
#         <li ><a href="Tekstbasert%20spill%202.ipynb">Tekstbasert spill 2</a></li>
#     <li ><a href="Geometrisk%20rekke.ipynb">Geometrisk rekke</a></li>
#     <li ><a href="Fibonacci.ipynb">Fibonacci</a></li>
#     <li><a href="Alternerende%20sum.ipynb">Alternerende sum</a></li>
#     <li ><a href="Hangman.ipynb">Hangman</a></li>
#     <li ><a href="Doble%20lokker.ipynb">Doble løkker</a></li>
#     </ul>
#   </div>
# </nav>
# 
# # Kodeforståelse
# 
# **Læringsmål:**
# 
# * Tolke kode
# 
# Koden under kan ikke kjøres, her skal du tenke deg fram til svarene! Ca. 20% av eksamen er kodeforståelse så se på dette som god trening! 

# **a)** Hva skrives ut i koden under?

# ```python
# a=345
# b=''
# while a or b=='':
#     b=str(a%2)+b
#     a=a//2
# print(b)
# ```

# 010110001

# **b)** Hva skrives ut i koden under?

# ```python
# for x in range(0, 10, 2):
#     print(x, end='')
#     if x%4==0:
#         print( ": Dette tallet går opp i 4-gangern")
#     else:
#         print()
#      ```
#      
# `end=""` gjør at det neste som printes ikke printes en linje under, men at det fortsetter på samme linje.

# 0: Dette tallet går opp i 4-gangen
# 2 
# 4: Dette tallet går opp i 4-gangen 
# 6 
# 8: Dette tallet går opp i 4-gangen

# **c)** Hva skrives ut i koden under?

# ```python
# i = 1
# while i<10:
#     i = i*2
# print(i)
# ```

# 16

# **d)** Hva skrives ut i koden under?

# ```python
# i = 1
# j = 3
# while j>0:
#     i = i*2
#     j = j - 1
# print(i)```

# 8

# **e)** Hva skrives ut i koden under?
# 
# ```python
# i = 5
# for x in range(i):
#     for y in range(x+1):
#         print("*", end="")
#     print()```
#     
# Her er det en dobbel løkke, så dette er nok nytt for mange. Prøv likevel! Hvordan fungerer egentlig en løkke i en løkke? Se side 176 i Starting Out with Python.

# *
# **
# ***
# ****
