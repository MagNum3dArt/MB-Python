import pyfbsdk

selected_objects = FBModelList()
FBGetSelectedModels(selected_objects, None, True, True)
test_object = selected_objects[-1]
##test_object = FBFindModelByLabelName('OLD:second:marker') if FBFindModelByLabelName('OLD:second:marker') else FBFindModelByLabelName('marker')
##test_object.Selected = True
namespace_splitter = ':'
split_long_name_list = test_object.LongName.split(namespace_splitter)
namespaces_list  = test_object.LongName.split(namespace_splitter)
del(namespaces_list[-1])
print namespaces_list
print split_long_name_list
namespace = namespace_splitter.join(namespaces_list)
##namespace =  split_long_name_list[0] if len(split_long_name_list) > 1 else ""
name = split_long_name_list[-1]
object_type = test_object.FullName.split('::')[0]
#print test_object, test_object.Name, test_object.LongName, test_object.FullName, namespace, object_type

print "namespace is -%s-"  % namespace
print "name  is:%s:"  % name 
##test_object.ProcessNamespaceHierarchy (FBNamespaceAction.kFBRemoveAllNamespace,'')
##test_object.ProcessNamespaceHierarchy (FBNamespaceAction.kFBConcatNamespace,'OLD')