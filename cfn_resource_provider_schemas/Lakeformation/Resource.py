SCHEMA = {
  "typeName" : "AWS::LakeFormation::Resource",
  "description" : "Resource Type definition for AWS::LakeFormation::Resource",
  "additionalProperties" : False,
  "properties" : {
    "ResourceArn" : {
      "type" : "string"
    },
    "WithFederation" : {
      "type" : "boolean"
    },
    "Id" : {
      "type" : "string"
    },
    "HybridAccessEnabled" : {
      "type" : "boolean"
    },
    "UseServiceLinkedRole" : {
      "type" : "boolean"
    },
    "RoleArn" : {
      "type" : "string"
    }
  },
  "required" : [ "ResourceArn", "UseServiceLinkedRole" ],
  "createOnlyProperties" : [ "/properties/ResourceArn" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}