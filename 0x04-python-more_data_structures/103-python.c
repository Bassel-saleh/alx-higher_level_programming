#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print info about python list
 * @p: PyObject list
 */
void print_python_list(PyObject *p)
{
	int size_p, alloc_p, j;
	const char *type;
	PyListObject *list = (PyListObject *)p;
	PyVarObject *var = (PyVarObject *)p;

	size_p = var->ob_size;
	alloc_p = list->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size_p);
	printf("[*] Allocated = %d\n", alloc_p);
	for (j = 0; j < size_p; j++)
	{
		type = list->ob_item[j]->ob_type->tp_name;
		printf("Element %d: %s\n", j, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(list->ob_item[j]);
	}
}

/**
 * print_python_bytes - print info about python byte objects
 * @p: PyObject byte object
 */
void print_python_bytes(PyObject *p)
{
	unsigned char j, size_p;
	PyBytesObject *bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (strcmp(p->ob_type->tp_name, "bytes") != 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	printf("  size: %ld\n", ((PyVarObject *)p)->ob_size);
	printf("  trying string: %s\n", bytes->ob_sval);
	if (((PyVarObject *)p)->ob_size > 10)
		size_p = 10;
	else
		size_p = ((PyVarObject *)p)->ob_size + 1;
	printf("  first %d bytes: ", size_p);
	for (j = 0; j < size_p; j++)
	{
		printf("%02hhx", bytes->ob_sval[j]);
		if (j == (size_p - 1))
			printf("\n");
		else
			printf(" ");
	}
}
