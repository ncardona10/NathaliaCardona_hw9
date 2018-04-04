cpp_vs_python.png: times_cpp.csv times_python.csv
	python NathaliaCardona_Graficas.py
times_python.csv:
	python NathaliaCardona_GenerarTiempos.py > times_python.csv
times_cpp.csv: gen_times.x
	./gen_times.x > times_cpp.csv
gen_times.x:
	c++ NathaliaCardona_GenerarTiempos.cpp -o gen_times.x
clean:
	rm *.csv
	rm *.png
	rm *.x
