SCHEMA = {
  "typeName" : "AWS::CloudFormation::ModuleDefaultVersion",
  "description" : "A module that has been registered in the CloudFormation registry as the default version",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-cloudformation",
  "properties" : {
    "Arn" : {
      "description" : "The Amazon Resource Name (ARN) of the module version to set as the default version.",
      "pattern" : "^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/module/.+/[0-9]{8}$",
      "type" : "string"
    },
    "ModuleName" : {
      "description" : "The name of a module existing in the registry.",
      "pattern" : "^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::MODULE",
      "type" : "string"
    },
    "VersionId" : {
      "description" : "The ID of an existing version of the named module to set as the default.",
      "pattern" : "^[0-9]{8}$",
      "type" : "string"
    }
  },
  "oneOf" : [ {
    "required" : [ "Arn" ]
  }, {
    "required" : [ "ModuleName", "VersionId" ]
  } ],
  "createOnlyProperties" : [ "/properties/Arn", "/properties/ModuleName", "/properties/VersionId" ],
  "writeOnlyProperties" : [ "/properties/ModuleName", "/properties/VersionId" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "additionalIdentifiers" : [ [ "/properties/ModuleName" ] ],
  "handlers" : {
    "create" : {
      "permissions" : [ "cloudformation:DescribeType", "cloudformation:SetTypeDefaultVersion" ]
    },
    "delete" : {
      "permissions" : [ ]
    },
    "read" : {
      "permissions" : [ "cloudformation:DescribeType" ]
    },
    "list" : {
      "permissions" : [ "cloudformation:ListTypes" ]
    }
  },
  "additionalProperties" : False
}