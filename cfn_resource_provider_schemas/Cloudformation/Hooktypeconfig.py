SCHEMA = {
  "typeName" : "AWS::CloudFormation::HookTypeConfig",
  "description" : "Specifies the configuration data for a registered hook in CloudFormation Registry.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudformation",
  "properties" : {
    "TypeArn" : {
      "description" : "The Amazon Resource Name (ARN) of the type without version number.",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$",
      "type" : "string"
    },
    "TypeName" : {
      "description" : "The name of the type being registered.\n\nWe recommend that type names adhere to the following pattern: company_or_organization::service::type.",
      "pattern" : "^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$",
      "type" : "string"
    },
    "ConfigurationArn" : {
      "description" : "The Amazon Resource Name (ARN) for the configuration data, in this account and region.",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type(-configuration)?/hook/.+$",
      "type" : "string"
    },
    "Configuration" : {
      "description" : "The configuration data for the extension, in this account and region.",
      "pattern" : "[\\s\\S]+",
      "type" : "string"
    },
    "ConfigurationAlias" : {
      "description" : "An alias by which to refer to this extension configuration data.",
      "pattern" : "^[a-zA-Z0-9]{1,256}$",
      "default" : "default",
      "enum" : [ "default" ],
      "type" : "string"
    }
  },
  "oneOf" : [ {
    "required" : [ "TypeArn", "Configuration" ]
  }, {
    "required" : [ "TypeName", "Configuration" ]
  } ],
  "readOnlyProperties" : [ "/properties/ConfigurationArn" ],
  "createOnlyProperties" : [ "/properties/ConfigurationAlias" ],
  "primaryIdentifier" : [ "/properties/ConfigurationArn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:SetTypeConfiguration" ]
    },
    "read" : {
      "permissions" : [ "cloudformation:BatchDescribeTypeConfigurations" ]
    },
    "update" : {
      "permissions" : [ "cloudformation:SetTypeConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "cloudformation:SetTypeConfiguration" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "TypeName" : {
            "$ref" : "resource-schema.json#/properties/TypeName"
          },
          "TypeArn" : {
            "$ref" : "resource-schema.json#/properties/TypeArn"
          }
        }
      },
      "permissions" : [ "cloudformation:ListTypes", "cloudformation:BatchDescribeTypeConfigurations" ]
    }
  },
  "additionalProperties" : False
}