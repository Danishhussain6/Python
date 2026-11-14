 #Q : A runner completes a race in t=3725 seconds.
# write  python program to convert total time into hours, minutes  , and seconds
# Expected output :10h 20 min 50 s
t=3725
print(t//3600,"h" ,t%3600//60,"min",t%60,"s")
