SCHEMA = {
  "typeName" : "AWS::ServiceCatalogAppRegistry::AttributeGroup",
  "description" : "Resource Schema for AWS::ServiceCatalogAppRegistry::AttributeGroup.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-servicecatalog-appregistry.git",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-appregistry-attributegroup.html",
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
      "pattern" : "[a-z0-9]{12}"
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "arn:aws[-a-z]*:servicecatalog:[a-z]{2}(-gov)?-[a-z]+-\\d:\\d{12}:/attribute-groups/[a-z0-9]+"
    },
    "Name" : {
      "type" : "string",
      "description" : "The name of the attribute group. ",
      "minLength" : 1,
      "maxLength" : 256,
      "pattern" : "\\w+"
    },
    "Description" : {
      "type" : "string",
      "description" : "The description of the attribute group. ",
      "maxLength" : 1024
    },
    "Attributes" : {
      "type" : "object"
    },
    "Tags" : {
      "$ref" : "#/definitions/Tags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "Name", "Attributes" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ],
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
      "permissions" : [ "servicecatalog:CreateAttributeGroup", "servicecatalog:TagResource" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:GetAttributeGroup" ]
    },
    "update" : {
      "permissions" : [ "servicecatalog:GetAttributeGroup", "servicecatalog:UpdateAttributeGroup", "servicecatalog:ListTagsForResource", "servicecatalog:TagResource", "servicecatalog:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DeleteAttributeGroup" ]
    },
    "list" : {
      "permissions" : [ "servicecatalog:ListAttributeGroups" ]
    }
  }
}