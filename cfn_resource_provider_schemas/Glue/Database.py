SCHEMA = {
  "typeName" : "AWS::Glue::Database",
  "description" : "Resource Type definition for AWS::Glue::Database",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-glue.git",
  "additionalProperties" : False,
  "properties" : {
    "CatalogId" : {
      "type" : "string",
      "description" : "The AWS account ID for the account in which to create the catalog object."
    },
    "DatabaseInput" : {
      "$ref" : "#/definitions/DatabaseInput",
      "description" : "The metadata for the database."
    },
    "DatabaseName" : {
      "type" : "string",
      "description" : "The name of the database. For hive compatibility, this is folded to lowercase when it is store."
    }
  },
  "definitions" : {
    "DatabaseIdentifier" : {
      "type" : "object",
      "description" : "A structure that describes a target database for resource linking.",
      "additionalProperties" : False,
      "properties" : {
        "DatabaseName" : {
          "type" : "string",
          "description" : "The name of the catalog database."
        },
        "Region" : {
          "type" : "string",
          "description" : "Region of the target database."
        },
        "CatalogId" : {
          "type" : "string",
          "description" : "The ID of the Data Catalog in which the database resides."
        }
      }
    },
    "PrincipalPrivileges" : {
      "type" : "object",
      "description" : "The permissions granted to a principal.",
      "additionalProperties" : False,
      "properties" : {
        "Permissions" : {
          "type" : "array",
          "description" : "The permissions that are granted to the principal.",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "type" : "string"
          }
        },
        "Principal" : {
          "$ref" : "#/definitions/DataLakePrincipal",
          "description" : "The principal who is granted permissions."
        }
      }
    },
    "DataLakePrincipal" : {
      "type" : "object",
      "description" : "The AWS Lake Formation principal.",
      "additionalProperties" : False,
      "properties" : {
        "DataLakePrincipalIdentifier" : {
          "type" : "string",
          "description" : "An identifier for the AWS Lake Formation principal."
        }
      }
    },
    "FederatedDatabase" : {
      "type" : "object",
      "description" : "A FederatedDatabase structure that references an entity outside the AWS Glue Data Catalog.",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionName" : {
          "type" : "string",
          "description" : "The name of the connection to the external metastore."
        },
        "Identifier" : {
          "type" : "string",
          "description" : "A unique identifier for the federated database."
        }
      }
    },
    "DatabaseInput" : {
      "type" : "object",
      "description" : "The structure used to create or update a database.",
      "additionalProperties" : False,
      "properties" : {
        "LocationUri" : {
          "type" : "string",
          "description" : "The location of the database (for example, an HDFS path)."
        },
        "CreateTableDefaultPermissions" : {
          "type" : "array",
          "description" : "Creates a set of default permissions on the table for principals. Used by AWS Lake Formation. Not used in the normal course of AWS Glue operations.",
          "uniqueItems" : False,
          "insertionOrder" : False,
          "items" : {
            "$ref" : "#/definitions/PrincipalPrivileges",
            "description" : "The permissions granted to a principal."
          }
        },
        "Description" : {
          "type" : "string",
          "description" : "A description of the database."
        },
        "Parameters" : {
          "type" : "object",
          "description" : "These key-value pairs define parameters and properties of the database."
        },
        "TargetDatabase" : {
          "$ref" : "#/definitions/DatabaseIdentifier",
          "description" : "A DatabaseIdentifier structure that describes a target database for resource linking."
        },
        "FederatedDatabase" : {
          "$ref" : "#/definitions/FederatedDatabase",
          "description" : "A FederatedDatabase structure that references an entity outside the AWS Glue Data Catalog."
        },
        "Name" : {
          "type" : "string",
          "description" : "The name of the database. For hive compatibility, this is folded to lowercase when it is stored."
        }
      }
    }
  },
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "required" : [ "DatabaseInput", "CatalogId" ],
  "createOnlyProperties" : [ "/properties/DatabaseName" ],
  "primaryIdentifier" : [ "/properties/DatabaseName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "glue:CreateDatabase", "glue:GetDatabase", "glue:PassConnection", "glue:CreateConnection", "lakeformation:ListResources", "lakeformation:DescribeResource", "lakeformation:DescribeLakeFormationIdentityCenterConfiguration" ]
    },
    "read" : {
      "permissions" : [ "glue:GetDatabase", "glue:GetConnection", "lakeformation:ListResources", "lakeformation:DescribeResource", "lakeformation:DescribeLakeFormationIdentityCenterConfiguration" ]
    },
    "update" : {
      "permissions" : [ "glue:UpdateDatabase", "glue:UpdateConnection", "lakeformation:ListResources", "lakeformation:DescribeResource", "lakeformation:DescribeLakeFormationIdentityCenterConfiguration" ]
    },
    "delete" : {
      "permissions" : [ "glue:DeleteDatabase", "glue:GetDatabase", "glue:DeleteConnection", "glue:GetConnection", "lakeformation:ListResources", "lakeformation:DescribeResource", "lakeformation:DescribeLakeFormationIdentityCenterConfiguration" ]
    },
    "list" : {
      "permissions" : [ "glue:GetDatabases", "lakeformation:ListResources", "lakeformation:DescribeResource", "lakeformation:DescribeLakeFormationIdentityCenterConfiguration" ]
    }
  }
}