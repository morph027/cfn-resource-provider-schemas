SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::TagOptionAssociation",
  "description" : "Resource Type definition for AWS::ServiceCatalog::TagOptionAssociation",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "TagOptionId" : {
      "type" : "string"
    },
    "ResourceId" : {
      "type" : "string"
    }
  },
  "required" : [ "TagOptionId", "ResourceId" ],
  "createOnlyProperties" : [ "/properties/TagOptionId", "/properties/ResourceId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}