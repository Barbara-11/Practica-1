#Mostrar Checksum
echo "Checksum de fcfm.png"
md5sum fcfm.png > archivo1.txt
cat archivo1.txt
echo -e "\n"


echo "Checksum de msg.txt"
md5sum fcfm.png > archivo2.txt
cat archivo2.txt
echo -e "\n"


echo "Checksum de mystery_img1.txt"
md5sum fcfm.png > archivo3.txt
cat archivo3.txt
echo -e "\n"


echo "Checksum de mystery_img2.txt"
md5sum fcfm.png > archivo4.txt
cat archivo4.txt
echo -e "\n"

#Codificacion
echo "Primer archivo a codificar"
echo "Escriba fcfm.png"
read archivo
base64 < $archivo > texto1.txt
echo -e "Texto guardado como texto1 \n" 


echo "Segundo archivo a codificar"
echo "Escriba msg.txt"
read archivo
base64 < $archivo > texto2.txt
echo -e "Texto guardado como texto2 \n"

#Decodificacion
echo "Primer archivo a decodificar"
echo "Escriba mystery_img1.txt"
read archivo
base64 -d < $archivo > imagen1.png
echo -e "Texto guardado como imagen1 \n"

echo "Segundo archivo a decodificar"
echo "Escriba mystery_img2.txt"
read archivo
base64 -d < $archivo > imagen2.png
echo -e "Texto guardado como imagen2 \n"





