SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::ServiceAction",
  "description" : "Resource Schema for AWS::ServiceCatalog::ServiceAction",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "DefinitionParameter" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1000
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 4096
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    }
  },
  "properties" : {
    "AcceptLanguage" : {
      "type" : "string",
      "enum" : [ "en", "jp", "zh" ]
    },
    "Name" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "DefinitionType" : {
      "type" : "string",
      "enum" : [ "SSM_AUTOMATION" ]
    },
    "Definition" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/DefinitionParameter"
      }
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 1024
    },
    "Id" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Id" ],
  "writeOnlyProperties" : [ "/properties/AcceptLanguage" ],
  "readOnlyProperties" : [ "/properties/Id" ],
  "required" : [ "Name", "DefinitionType", "Definition" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:CreateServiceAction", "ssm:DescribeDocument", "iam:GetRole" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:DescribeServiceAction" ]
    },
    "update" : {
      "permissions" : [ "servicecatalog:UpdateServiceAction", "iam:GetRole", "ssm:DescribeDocument" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DeleteServiceAction" ]
    },
    "list" : {
      "permissions" : [ "servicecatalog:ListServiceActions" ]
    }
  }
}