SCHEMA = {
  "typeName" : "AWS::CloudFormation::HookDefaultVersion",
  "description" : "Set a version as default version for a hook in CloudFormation Registry.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudformation",
  "properties" : {
    "TypeVersionArn" : {
      "description" : "The Amazon Resource Name (ARN) of the type version.",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$",
      "type" : "string"
    },
    "TypeName" : {
      "description" : "The name of the type being registered.\n\nWe recommend that type names adhere to the following pattern: company_or_organization::service::type.",
      "pattern" : "^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$",
      "type" : "string"
    },
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the type. This is used to uniquely identify a HookDefaultVersion",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$",
      "type" : "string"
    },
    "VersionId" : {
      "description" : "The ID of an existing version of the hook to set as the default.",
      "pattern" : "^[A-Za-z0-9-]{1,128}$",
      "type" : "string"
    }
  },
  "oneOf" : [ {
    "required" : [ "TypeVersionArn" ]
  }, {
    "required" : [ "TypeName", "VersionId" ]
  } ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:SetTypeDefaultVersion" ]
    },
    "read" : {
      "permissions" : [ "cloudformation:DescribeType" ]
    },
    "update" : {
      "permissions" : [ "cloudformation:SetTypeDefaultVersion" ]
    },
    "delete" : {
      "permissions" : [ ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TypeName" : {
            "$ref" : "resource-schema.json#/properties/TypeName"
          }
        }
      },
      "permissions" : [ "cloudformation:ListTypes" ]
    }
  },
  "additionalProperties" : False
}