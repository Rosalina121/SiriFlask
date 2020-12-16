import ctypes

# defines
EVERYTHING_REQUEST_FILE_NAME = 0x00000001
EVERYTHING_REQUEST_PATH = 0x00000002
EVERYTHING_REQUEST_FULL_PATH_AND_FILE_NAME = 0x00000004
EVERYTHING_REQUEST_EXTENSION = 0x00000008
EVERYTHING_REQUEST_SIZE = 0x00000010
EVERYTHING_REQUEST_DATE_CREATED = 0x00000020
EVERYTHING_REQUEST_DATE_MODIFIED = 0x00000040
EVERYTHING_REQUEST_DATE_ACCESSED = 0x00000080
EVERYTHING_REQUEST_ATTRIBUTES = 0x00000100
EVERYTHING_REQUEST_FILE_LIST_FILE_NAME = 0x00000200
EVERYTHING_REQUEST_RUN_COUNT = 0x00000400
EVERYTHING_REQUEST_DATE_RUN = 0x00000800
EVERYTHING_REQUEST_DATE_RECENTLY_CHANGED = 0x00001000
EVERYTHING_REQUEST_HIGHLIGHTED_FILE_NAME = 0x00002000
EVERYTHING_REQUEST_HIGHLIGHTED_PATH = 0x00004000
EVERYTHING_REQUEST_HIGHLIGHTED_FULL_PATH_AND_FILE_NAME = 0x00008000

DLL_PATH = "C:\\Users\\kapits\\PycharmProjects\\SiriFlask\\EverythingSDK\\dll\\Everything64.dll"

# dll imports
everything_dll = ctypes.WinDLL(DLL_PATH)
everything_dll.Everything_GetResultDateModified.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ulonglong)]
everything_dll.Everything_GetResultSize.argtypes = [ctypes.c_int, ctypes.POINTER(ctypes.c_ulonglong)]


def get_filename(request):
    # create buffers
    filename = ctypes.create_unicode_buffer(260)
    temp = []
    ret_dict = {'files': temp, 'count': 0}

    # setup search
    everything_dll.Everything_SetSearchW(request)
    everything_dll.Everything_SetRequestFlags(
        EVERYTHING_REQUEST_FILE_NAME | EVERYTHING_REQUEST_PATH | EVERYTHING_REQUEST_SIZE | EVERYTHING_REQUEST_DATE_MODIFIED)

    # execute the query
    everything_dll.Everything_QueryW(1)

    # get the number of results
    num_results = everything_dll.Everything_GetNumResults()
    ret_dict['count'] = num_results
    for i in range(num_results):
        everything_dll.Everything_GetResultFullPathNameW(i, filename, 260)
        ret_dict['files'].append(format(ctypes.wstring_at(filename)))

    return ret_dict
