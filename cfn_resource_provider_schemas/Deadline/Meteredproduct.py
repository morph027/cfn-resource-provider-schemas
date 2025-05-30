SCHEMA = {
  "typeName" : "AWS::Deadline::MeteredProduct",
  "description" : "Definition of AWS::Deadline::MeteredProduct Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-deadline",
  "properties" : {
    "LicenseEndpointId" : {
      "type" : "string",
      "pattern" : "^le-[0-9a-f]{32}$"
    },
    "ProductId" : {
      "type" : "string",
      "pattern" : "^[0-9a-z]{1,32}-[.0-9a-z]{1,32}$"
    },
    "Port" : {
      "type" : "integer",
      "minimum" : 1024,
      "maximum" : 65535
    },
    "Family" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Vendor" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64
    },
    "Arn" : {
      "type" : "string",
      "pattern" : "^arn:(aws[a-zA-Z-]*):deadline:[a-z0-9-]+:[0-9]{12}:license-endpoint/le-[0-9a-z]{32}/metered-product/[0-9a-z]{1,32}-[.0-9a-z]{1,32}"
    }
  },
  "createOnlyProperties" : [ "/properties/LicenseEndpointId", "/properties/ProductId" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/Port", "/properties/Family", "/properties/Vendor" ],
  "primaryIdentifier" : [ "/properties/Arn" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:PutMeteredProduct", "deadline:ListMeteredProducts" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetMeteredProduct", "deadline:ListMeteredProducts" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteMeteredProduct", "deadline:ListMeteredProducts" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "LicenseEndpointId" : {
            "$ref" : "resource-schema.json#/properties/LicenseEndpointId"
          }
        },
        "required" : [ "LicenseEndpointId" ]
      },
      "permissions" : [ "deadline:ListMeteredProducts" ]
    }
  },
  "additionalProperties" : False
}