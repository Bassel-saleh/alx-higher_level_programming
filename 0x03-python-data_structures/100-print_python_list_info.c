#include <python.h>
/**
 * print_python_list_info - print info of a python list
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int size_p, alloc_p, j;
	pyObject *obj;

	size_p = Py_SIZE(p);
	alloc_p = ((PyListObject *)p)->allocated;
	printf("[*] size of the pythone List = %d\n", size_p);
	printf("[*] Allocated = %d\n", alloc_p);
	for (j = 0; j < size_p; j++)
	{
		printf("Element %d: ", j);
		obj = PyList_GetItem(p, j);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
