SCHEMA = {
  "typeName" : "AWS::AppStream::Entitlement",
  "description" : "Resource Type definition for AWS::AppStream::Entitlement",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-appstream.git",
  "definitions" : {
    "Attribute" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string"
        },
        "Value" : {
          "type" : "string"
        }
      },
      "required" : [ "Name", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Name" : {
      "type" : "string"
    },
    "StackName" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "AppVisibility" : {
      "type" : "string"
    },
    "Attributes" : {
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Attribute"
      }
    },
    "CreatedTime" : {
      "type" : "string"
    },
    "LastModifiedTime" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "Name", "StackName", "AppVisibility", "Attributes" ],
  "readOnlyProperties" : [ "/properties/CreatedTime", "/properties/LastModifiedTime" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/StackName" ],
  "primaryIdentifier" : [ "/properties/StackName", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "appstream:CreateEntitlement" ]
    },
    "read" : {
      "permissions" : [ "appstream:DescribeEntitlements" ]
    },
    "update" : {
      "permissions" : [ "appstream:UpdateEntitlement" ]
    },
    "delete" : {
      "permissions" : [ "appstream:DeleteEntitlement" ]
    }
  }
}