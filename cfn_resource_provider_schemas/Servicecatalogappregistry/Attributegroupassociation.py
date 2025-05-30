SCHEMA = {
  "typeName" : "AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation",
  "description" : "Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroupAssociation.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-servicecatalog-appregistry",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-appregistry-attributegroupassociation.html",
  "properties" : {
    "Application" : {
      "type" : "string",
      "description" : "The name or the Id of the Application.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "\\w+|[a-z0-9]{12}"
    },
    "AttributeGroup" : {
      "type" : "string",
      "description" : "The name or the Id of the AttributeGroup.",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "\\w+|[a-z0-9]{12}"
    },
    "ApplicationArn" : {
      "type" : "string",
      "pattern" : "arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/applications/[a-z0-9]+"
    },
    "AttributeGroupArn" : {
      "type" : "string",
      "pattern" : "arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/attribute-groups/[a-z0-9]+"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Application", "AttributeGroup" ],
  "readOnlyProperties" : [ "/properties/ApplicationArn", "/properties/AttributeGroupArn" ],
  "createOnlyProperties" : [ "/properties/Application", "/properties/AttributeGroup" ],
  "primaryIdentifier" : [ "/properties/ApplicationArn", "/properties/AttributeGroupArn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:AssociateAttributeGroup" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:ListAttributeGroupsForApplication" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DisassociateAttributeGroup" ]
    },
    "list" : {
      "permissions" : [ "servicecatalog:ListAttributeGroupsForApplication" ],
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