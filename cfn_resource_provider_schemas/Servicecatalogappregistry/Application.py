SCHEMA = {
  "typeName" : "AWS::ServiceCatalogAppRegistry::Application",
  "description" : "Resource Schema for AWS::ServiceCatalogAppRegistry::Application",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-servicecatalog-appregistry.git",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-appregistry-application.html",
  "definitions" : {
    "Tags" : {
      "type" : "object",
      "patternProperties" : {
        "^[a-zA-Z+-=._:/]+$" : {
          "type" : "string",
          "maxLength" : 256
        }
      },
      "maxProperties" : 50,
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Id" : {
      "type" : "string",
      "pattern" : "[a-z0-9]{26}"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/applications/[a-z0-9]+"
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the application. ",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "\\w+"
    },
    "Description" : {
      "type" : "string",
      "description" : "The description of the application. ",
      "maxLength" : 1024
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    },
    "ApplicationTagKey" : {
      "type" : "string",
      "description" : "The key of the AWS application tag, which is awsApplication. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value.",
      "maxLength" : 128,
      "pattern" : "\\w+"
    },
    "ApplicationTagValue" : {
      "type" : "string",
      "description" : "The value of the AWS application tag, which is the identifier of an associated resource. Applications created before 11/13/2023 or applications without the AWS application tag resource group return no value. ",
      "maxLength" : 256,
      "pattern" : "\\[a-zA-Z0-9_-:/]+"
    },
    "ApplicationName" : {
      "type" : "string",
      "description" : "The name of the application. ",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "\\w+"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn", "/properties/ApplicationName", "/properties/ApplicationTagKey", "/properties/ApplicationTagValue" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "additionalIdentifiers" : [ [ "/properties/Name" ] ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "servicecatalog:TagResource", "servicecatalog:UntagResource", "servicecatalog:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:CreateApplication", "servicecatalog:TagResource", "iam:CreateServiceLinkedRole" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:GetApplication" ]
    },
    "update" : {
      "permissions" : [ "servicecatalog:GetApplication", "servicecatalog:ListTagsForResource", "servicecatalog:TagResource", "servicecatalog:UntagResource", "servicecatalog:UpdateApplication", "iam:CreateServiceLinkedRole" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DeleteApplication" ]
    },
    "list" : {
      "permissions" : [ "servicecatalog:ListApplications" ]
    }
  }
}