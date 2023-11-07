#include <python.h>
/**
 * print_python_list_info - prints py info
 * @z: varisbl
 */
void print_python_list_info(PyObject *z)
{
	int x, i;
	PyObject *ob;
	int y;

	y = 0;
	alc = ((PyListObject *)z)->allocated;
	x = Py_SIZE(z);

	printf("[*] size of the Python Lis = %d \n", x);
	printf("[*] Allocated = %d \n", i);

	while (y  < size)
	{
		printf("Element %d: ", y);
		ob = PyList_GetItem(z, y);
		printf("%s\n", PyTYPE(ob)->ob_type);
		y++;
	}
}
