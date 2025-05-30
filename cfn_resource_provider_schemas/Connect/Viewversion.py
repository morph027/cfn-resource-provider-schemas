SCHEMA = {
  "typeName" : "AWS::Connect::ViewVersion",
  "description" : "Resource Type definition for AWS::Connect::ViewVersion",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-connect",
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "properties" : {
    "ViewArn" : {
      "description" : "The Amazon Resource Name (ARN) of the view for which a version is being created.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/view/[-:a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "ViewVersionArn" : {
      "description" : "The Amazon Resource Name (ARN) of the created view version.",
      "type" : "string",
      "pattern" : "^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*/view/[-:a-zA-Z0-9]*$",
      "minLength" : 1,
      "maxLength" : 255
    },
    "VersionDescription" : {
      "description" : "The description for the view version.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 4096,
      "pattern" : "^([\\p{L}\\p{N}_.:\\/=+\\-@,]+[\\p{L}\\p{Z}\\p{N}_.:\\/=+\\-@,]*)$"
    },
    "ViewContentSha256" : {
      "description" : "The view content hash to be checked.",
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 64,
      "pattern" : "^[a-zA-Z0-9]{64}$"
    },
    "Version" : {
      "description" : "The version of the view.",
      "type" : "integer"
    }
  },
  "required" : [ "ViewArn" ],
  "propertyTransform" : {
    "/properties/ViewArn" : "$join([\"^\", ViewArn, \":[0-9]*$\"])"
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "connect:CreateViewVersion" ]
    },
    "read" : {
      "permissions" : [ "connect:DescribeView" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ViewArn" : {
            "$ref" : "resource-schema.json#/properties/ViewArn"
          }
        },
        "required" : [ "ViewArn" ]
      },
      "permissions" : [ "connect:ListViewVersions" ]
    },
    "update" : {
      "permissions" : [ ]
    },
    "delete" : {
      "permissions" : [ "connect:DeleteViewVersion" ]
    }
  },
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/ViewVersionArn" ],
  "readOnlyProperties" : [ "/properties/ViewVersionArn", "/properties/Version" ],
  "createOnlyProperties" : [ "/properties/ViewArn", "/properties/ViewContentSha256" ]
}