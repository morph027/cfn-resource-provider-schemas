SCHEMA = {
  "typeName" : "AWS::OpsWorks::Volume",
  "description" : "Resource Type definition for AWS::OpsWorks::Volume",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Ec2VolumeId" : {
      "type" : "string"
    },
    "MountPoint" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    },
    "StackId" : {
      "type" : "string"
    }
  },
  "required" : [ "Ec2VolumeId", "StackId" ],
  "createOnlyProperties" : [ "/properties/StackId", "/properties/Ec2VolumeId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}