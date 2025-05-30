SCHEMA = {
  "typeName" : "AWS::Invoicing::InvoiceUnit",
  "description" : "An invoice unit is a set of mutually exclusive accounts that correspond to your business entity. Invoice units allow you to separate AWS account costs and configures your invoice for each business entity.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "InvoiceUnitArn" : {
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:[a-z0-9]+:[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+$",
      "minLength" : 1,
      "maxLength" : 256
    },
    "InvoiceReceiver" : {
      "type" : "string",
      "pattern" : "^\\d{12}$",
      "minLength" : 12,
      "maxLength" : 12
    },
    "Name" : {
      "type" : "string",
      "pattern" : "^(?! )[\\p{L}\\p{N}\\p{Z}-_]*(?<! )$",
      "minLength" : 1,
      "maxLength" : 50
    },
    "Description" : {
      "type" : "string",
      "pattern" : "^[\\S\\s]*$",
      "minLength" : 0,
      "maxLength" : 500
    },
    "TaxInheritanceDisabled" : {
      "type" : "boolean"
    },
    "Rule" : {
      "type" : "object",
      "properties" : {
        "LinkedAccounts" : {
          "type" : "array",
          "items" : {
            "type" : "string",
            "pattern" : "^\\d{12}$",
            "minLength" : 12,
            "maxLength" : 12
          }
        }
      },
      "required" : [ "LinkedAccounts" ],
      "additionalProperties" : False
    },
    "LastModified" : {
      "type" : "number"
    },
    "ResourceTag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256
        },
        "Value" : {
          "type" : "string",
          "minLength" : 0,
          "maxLength" : 200
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "ResourceTags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ResourceTag"
      }
    }
  },
  "properties" : {
    "InvoiceUnitArn" : {
      "$ref" : "#/definitions/InvoiceUnitArn"
    },
    "InvoiceReceiver" : {
      "$ref" : "#/definitions/InvoiceReceiver"
    },
    "Name" : {
      "$ref" : "#/definitions/Name"
    },
    "Description" : {
      "$ref" : "#/definitions/Description"
    },
    "TaxInheritanceDisabled" : {
      "$ref" : "#/definitions/TaxInheritanceDisabled"
    },
    "Rule" : {
      "$ref" : "#/definitions/Rule"
    },
    "LastModified" : {
      "$ref" : "#/definitions/LastModified"
    },
    "ResourceTags" : {
      "$ref" : "#/definitions/ResourceTags"
    }
  },
  "additionalProperties" : False,
  "required" : [ "InvoiceReceiver", "Name", "Rule" ],
  "primaryIdentifier" : [ "/properties/InvoiceUnitArn" ],
  "readOnlyProperties" : [ "/properties/InvoiceUnitArn", "/properties/LastModified" ],
  "createOnlyProperties" : [ "/properties/InvoiceReceiver", "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "invoicing:CreateInvoiceUnit", "invoicing:TagResource" ]
    },
    "read" : {
      "permissions" : [ "invoicing:GetInvoiceUnit", "invoicing:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "invoicing:UpdateInvoiceUnit", "invoicing:UntagResource", "invoicing:TagResource" ]
    },
    "delete" : {
      "permissions" : [ "invoicing:DeleteInvoiceUnit" ]
    },
    "list" : {
      "permissions" : [ "invoicing:ListInvoiceUnits" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/ResourceTags",
    "permissions" : [ "invoicing:TagResource", "invoicing:UntagResource", "invoicing:ListTagsForResource" ]
  }
}