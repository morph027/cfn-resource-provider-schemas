SCHEMA = {
  "typeName" : "AWS::EventSchemas::RegistryPolicy",
  "description" : "Resource Type definition for AWS::EventSchemas::RegistryPolicy",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Policy" : {
      "type" : "object"
    },
    "RegistryName" : {
      "type" : "string"
    },
    "RevisionId" : {
      "type" : "string"
    }
  },
  "required" : [ "RegistryName", "Policy" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "schemas:PutResourcePolicy", "schemas:GetResourcePolicy", "schemas:DescribeRegistry" ]
    },
    "delete" : {
      "permissions" : [ "schemas:DeleteResourcePolicy", "schemas:GetResourcePolicy" ]
    },
    "update" : {
      "permissions" : [ "schemas:PutResourcePolicy", "schemas:GetResourcePolicy" ]
    },
    "read" : {
      "permissions" : [ "schemas:GetResourcePolicy" ]
    }
  },
  "tagging" : {
    "taggable" : False
  }
}