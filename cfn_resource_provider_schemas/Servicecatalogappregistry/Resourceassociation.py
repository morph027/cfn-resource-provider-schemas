SCHEMA = {
  "typeName" : "AWS::ServiceCatalogAppRegistry::ResourceAssociation",
  "description" : "Resource Schema for AWS::ServiceCatalogAppRegistry::ResourceAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-servicecatalog-appregistry",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-appregistry-resourceassociation.html",
  "properties" : {
    "Application" : {
      "type" : "string",
      "description" : "The name or the Id of the Application.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "\\w+|[a-z0-9]{12}"
    },
    "Resource" : {
      "type" : "string",
      "description" : "The name or the Id of the Resource.",
      "pattern" : "\\w+|arn:aws[-a-z]*:cloudformation:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:stack/[a-zA-Z][-A-Za-z0-9]{0,127}/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}"
    },
    "ResourceType" : {
      "type" : "string",
      "description" : "The type of the CFN Resource for now it's enum CFN_STACK.",
      "enum" : [ "CFN_STACK" ]
    },
    "ApplicationArn" : {
      "type" : "string",
      "pattern" : "arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/applications/[a-z0-9]+"
    },
    "ResourceArn" : {
      "type" : "string",
      "pattern" : "arn:aws[-a-z]*:cloudformation:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:stack/[a-zA-Z][-A-Za-z0-9]{0,127}/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Application", "Resource", "ResourceType" ],
  "readOnlyProperties" : [ "/properties/ApplicationArn", "/properties/ResourceArn" ],
  "createOnlyProperties" : [ "/properties/Application", "/properties/Resource", "/properties/ResourceType" ],
  "primaryIdentifier" : [ "/properties/ApplicationArn", "/properties/ResourceArn", "/properties/ResourceType" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:AssociateResource", "cloudformation:DescribeStacks" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:ListAssociatedResources" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DisassociateResource" ]
    },
    "list" : {
      "permissions" : [ "servicecatalog:ListAssociatedResources" ],
      "handlerSchema" : {
        "properties" : {
          "ApplicationArn" : {
            "$ref" : "resource-schema.json#/properties/ApplicationArn"
          }
        },
        "required" : [ "ApplicationArn" ]
      }
    }
  }
}