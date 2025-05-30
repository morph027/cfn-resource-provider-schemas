SCHEMA = {
  "typeName" : "AWS::Lambda::LayerVersion",
  "description" : "Resource Type definition for AWS::Lambda::LayerVersion",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-lambda.git",
  "definitions" : {
    "Content" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "S3ObjectVersion" : {
          "description" : "For versioned objects, the version of the layer archive object to use.",
          "type" : "string"
        },
        "S3Bucket" : {
          "description" : "The Amazon S3 bucket of the layer archive.",
          "type" : "string"
        },
        "S3Key" : {
          "description" : "The Amazon S3 key of the layer archive.",
          "type" : "string"
        }
      },
      "required" : [ "S3Bucket", "S3Key" ]
    }
  },
  "properties" : {
    "CompatibleRuntimes" : {
      "description" : "A list of compatible function runtimes. Used for filtering with ListLayers and ListLayerVersions.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    },
    "LicenseInfo" : {
      "description" : "The layer's software license.",
      "type" : "string"
    },
    "Description" : {
      "description" : "The description of the version.",
      "type" : "string"
    },
    "LayerName" : {
      "description" : "The name or Amazon Resource Name (ARN) of the layer.",
      "type" : "string"
    },
    "Content" : {
      "description" : "The function layer archive.",
      "$ref" : "#/definitions/Content"
    },
    "LayerVersionArn" : {
      "type" : "string"
    },
    "CompatibleArchitectures" : {
      "description" : "A list of compatible instruction set architectures.",
      "type" : "array",
      "insertionOrder" : False,
      "uniqueItems" : False,
      "items" : {
        "type" : "string"
      }
    }
  },
  "additionalProperties" : False,
  "required" : [ "Content" ],
  "createOnlyProperties" : [ "/properties/CompatibleRuntimes", "/properties/LicenseInfo", "/properties/CompatibleArchitectures", "/properties/LayerName", "/properties/Description", "/properties/Content" ],
  "readOnlyProperties" : [ "/properties/LayerVersionArn" ],
  "writeOnlyProperties" : [ "/properties/Content" ],
  "primaryIdentifier" : [ "/properties/LayerVersionArn" ],
  "propertyTransform" : {
    "/properties/LayerName" : "$split(LayerName, \":\")[-1] $OR LayerName"
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "lambda:PublishLayerVersion", "s3:GetObject", "s3:GetObjectVersion" ]
    },
    "read" : {
      "permissions" : [ "lambda:GetLayerVersion" ]
    },
    "delete" : {
      "permissions" : [ "lambda:GetLayerVersion", "lambda:DeleteLayerVersion" ]
    },
    "list" : {
      "permissions" : [ "lambda:ListLayerVersions" ]
    }
  }
}